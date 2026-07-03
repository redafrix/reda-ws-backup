# Stage 6 Experiments: holdout_scene_kitchen_scene2

```json
{
  "split": "holdout_scene_kitchen_scene2",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 128,
      "best_calib_loss": 0.05412095785140991,
      "train_time_sec": 23.195348262786865,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9603418012549412,
            "spearman": 0.939308911458717,
            "auroc_top30_bad": 0.9994514761904761,
            "mae": 0.10989430589042604,
            "mse": 0.04568684012951279,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.547,
            "expert_lt_simvla_seed0": 0.973,
            "same_context_pred_std": 0.6705385549000369,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.2987518790103495
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3158005520388484
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4759103213660419
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.786687641667823
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9977223550403143,
            "spearman": 0.9979614967744109,
            "auroc_top30_worst": 0.9987885714285715,
            "pairwise_seed_ranking": 0.8966,
            "predicted_best_mean_error": 1.4549992519319057,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07331175166368498,
            "gap_to_oracle": 0.0030341300964356055,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5885229386091232
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7986244863510131
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0483627331733703
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2620041085561116
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.317758703231812,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3965765595701005,
                "rejected_mean_error": 2.5789215292930603,
                "gap_rejected_minus_accepted": 1.1823449697229598
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9249624013900757,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2620041085561116,
                "rejected_mean_error": 2.2732319005012513,
                "gap_rejected_minus_accepted": 1.0112277919451398
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5219994187355042,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0483627331733703,
                "rejected_mean_error": 1.9812593799114226,
                "gap_rejected_minus_accepted": 0.9328966467380524
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0988017320632935,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7986244863510131,
                "rejected_mean_error": 1.7535399132728577,
                "gap_rejected_minus_accepted": 0.9549154269218446
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.367416524887085,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4069503205683496,
                "rejected_mean_error": 2.6205571508407592,
                "gap_rejected_minus_accepted": 1.2136068302724097
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.948766052722931,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.270067666888237,
                "rejected_mean_error": 2.3030410137176514,
                "gap_rejected_minus_accepted": 1.0329733468294144
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5340274572372437,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.053319075167179,
                "rejected_mean_error": 2.003302932024002,
                "gap_rejected_minus_accepted": 0.9499838568568231
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1000092029571533,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8000532294511795,
                "rejected_mean_error": 1.771063594977061,
                "gap_rejected_minus_accepted": 0.9710103655258815
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8966126074814704,
            "spearman": 0.8686333686516842,
            "auroc_top30_bad": 0.9580929523809524,
            "mae": 0.3127365324020386,
            "mse": 0.17114488421461257,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.972,
            "same_context_pred_std": 0.7207057560711951,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.3460652651786804
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.39510253007411955
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5584203575611114
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9369281143903733
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.8235426895717245,
            "spearman": 0.8247305786303566,
            "auroc_top30_worst": 0.9157150476190477,
            "pairwise_seed_ranking": 0.7664,
            "predicted_best_mean_error": 1.8439433892965318,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.07367603623867014,
            "gap_to_oracle": 0.018770486950874465,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0481044487953186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.194203172547695
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4076187843322754
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6613603389339406
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4931628465652467,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7860757359398736,
                "rejected_mean_error": 2.9395642137527465,
                "gap_rejected_minus_accepted": 1.153488477812873
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.211560368537903,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6606908179143705,
                "rejected_mean_error": 2.6220876462162495,
                "gap_rejected_minus_accepted": 0.961396828301879
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8295092582702637,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.4076187843322754,
                "rejected_mean_error": 2.3952303831100465,
                "gap_rejected_minus_accepted": 0.9876115987777712
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2513230443000793,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1955729865799316,
                "rejected_mean_error": 2.1372106561920305,
                "gap_rejected_minus_accepted": 0.9416376696120989
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5181904315948485,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7996012960539924,
                "rejected_mean_error": 2.9797825908660887,
                "gap_rejected_minus_accepted": 1.1801812948120962
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2595932483673096,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.664979450524172,
                "rejected_mean_error": 2.667519033901275,
                "gap_rejected_minus_accepted": 1.0025395833771031
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.8925318717956543,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4238212294578552,
                "rejected_mean_error": 2.4114176216125487,
                "gap_rejected_minus_accepted": 0.9875963921546935
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.290183663368225,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1712003255647325,
                "rejected_mean_error": 2.1690868228514564,
                "gap_rejected_minus_accepted": 0.9978864972867239
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.8061923161711486,
            "spearman": 0.8272803922720096,
            "auroc_top30_bad": 0.9632053333333335,
            "mae": 0.3971713715314865,
            "mse": 0.3458818911984015,
            "expert_lt_perturb_large": 0.996,
            "expert_lt_other_task": 0.516,
            "expert_lt_simvla_seed0": 0.956,
            "same_context_pred_std": 0.659570806289705,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4083825432658196
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.40857233426570894
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5142930530786515
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8437006480534871
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.6923703351365729,
            "spearman": 0.7570513389128569,
            "auroc_top30_worst": 0.841127619047619,
            "pairwise_seed_ranking": 0.7708,
            "predicted_best_mean_error": 1.6737477642297744,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.05425247013568879,
            "gap_to_oracle": 0.022219061613082847,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.694569375038147
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8414079143832891
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1790204392433166
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4199196013814606
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3659552812576297,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6258433668348524,
                "rejected_mean_error": 2.6004239749908447,
                "gap_rejected_minus_accepted": 0.9745806081559922
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.077257752418518,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4179653902572908,
                "rejected_mean_error": 2.6373585108370063,
                "gap_rejected_minus_accepted": 1.2193931205797155
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5113765001296997,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1790204392433166,
                "rejected_mean_error": 2.2675824160575866,
                "gap_rejected_minus_accepted": 1.08856197681427
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0059691667556763,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8411295076909537,
                "rejected_mean_error": 2.0179863913082134,
                "gap_rejected_minus_accepted": 1.1768568836172597
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.384774661064148,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5978728630807664,
                "rejected_mean_error": 2.8991465759277344,
                "gap_rejected_minus_accepted": 1.301273712846968
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0916755199432373,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4111154975100635,
                "rejected_mean_error": 2.6685946120156183,
                "gap_rejected_minus_accepted": 1.2574791145055548
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4951055645942688,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1841162352561951,
                "rejected_mean_error": 2.2718842334747316,
                "gap_rejected_minus_accepted": 1.0877679982185364
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.004193052649498,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8433383495088608,
                "rejected_mean_error": 2.026041404129987,
                "gap_rejected_minus_accepted": 1.1827030546211263
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.8563961330194073,
            "spearman": 0.8390962789206781,
            "auroc_top30_bad": 0.9089771622934888,
            "mae": 0.29946102854396617,
            "mse": 0.16199620611739102,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.5214285714285715,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.640767565650816,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.37731683275529315
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.3659473851323128
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.654580102775778
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9370192868085134
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.6663579545535223,
            "spearman": 0.5185115771373294,
            "auroc_top30_worst": 0.726588921282799,
            "pairwise_seed_ranking": 0.7921428571428571,
            "predicted_best_mean_error": 1.6287778041192464,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.06892467694623128,
            "gap_to_oracle": 0.014297302705901016,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.491967978647777
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.5027678431783404
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4809596569197518
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.561587697891962
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3358763933181765,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.594125251164512,
                "rejected_mean_error": 2.372225798879351,
                "gap_rejected_minus_accepted": 0.7781005477148388
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7524274289608002,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.561587697891962,
                "rejected_mean_error": 2.0029781300680978,
                "gap_rejected_minus_accepted": 0.4413904321761357
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4885928630828857,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4809596569197518,
                "rejected_mean_error": 1.86291095495224,
                "gap_rejected_minus_accepted": 0.3819512980324882
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0592893660068512,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.5027678431783404,
                "rejected_mean_error": 1.7283244601885477,
                "gap_rejected_minus_accepted": 0.22555661701020724
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.438577485084534,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.6145322701287648,
                "rejected_mean_error": 2.4462343794958934,
                "gap_rejected_minus_accepted": 0.8317021093671286
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7996367514133453,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.575329684075855,
                "rejected_mean_error": 2.0648208720343453,
                "gap_rejected_minus_accepted": 0.4894911879584902
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4996181726455688,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4950954045568194,
                "rejected_mean_error": 1.900309557574136,
                "gap_rejected_minus_accepted": 0.40521415301731656
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0941505134105682,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.5060136386326382,
                "rejected_mean_error": 1.7615987618764242,
                "gap_rejected_minus_accepted": 0.255585123243786
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
      "best_epoch": 157,
      "best_calib_loss": 0.01303210947662592,
      "train_time_sec": 28.487542390823364,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996400889769798,
            "spearman": 0.9989258338825795,
            "auroc_top30_bad": 0.9998286666666667,
            "mae": 0.014656070416091098,
            "mse": 0.00043822170962989703,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6684042072249685,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0007620483972132206
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16860389269441367
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4673482419721782
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7864680890396237
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9996470159535019,
            "spearman": 0.9996680115146966,
            "auroc_top30_worst": 0.9998750476190477,
            "pairwise_seed_ranking": 0.9424,
            "predicted_best_mean_error": 1.4528243931233882,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07548661047220251,
            "gap_to_oracle": 0.0008592712879180731,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.587019151210785
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7976937452316284
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.04767407913208
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2614878868103028
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2918753623962407,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3961499475108252,
                "rejected_mean_error": 2.582761037826538,
                "gap_rejected_minus_accepted": 1.1866110903157128
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9101866781711578,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2614878868103028,
                "rejected_mean_error": 2.274780565738678,
                "gap_rejected_minus_accepted": 1.0132926789283752
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5172818899154663,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.04767407913208,
                "rejected_mean_error": 1.981948033952713,
                "gap_rejected_minus_accepted": 0.9342739548206329
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0998035669326782,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7976937452316284,
                "rejected_mean_error": 1.7538501603126526,
                "gap_rejected_minus_accepted": 0.9561564150810242
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.335133957862854,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4065552101201482,
                "rejected_mean_error": 2.6241131448745727,
                "gap_rejected_minus_accepted": 1.2175579347544245
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.934525489807129,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2697481913963953,
                "rejected_mean_error": 2.3039994401931763,
                "gap_rejected_minus_accepted": 1.034251248796781
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5308048129081726,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0526440704464912,
                "rejected_mean_error": 2.00397793674469,
                "gap_rejected_minus_accepted": 0.9513338662981989
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1058306992053986,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7986797086000442,
                "rejected_mean_error": 1.7715214352607727,
                "gap_rejected_minus_accepted": 0.9728417266607284
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9846321385434053,
            "spearman": 0.9814902184665215,
            "auroc_top30_bad": 0.9897935238095239,
            "mae": 0.1307537615252193,
            "mse": 0.027021973356045954,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 0.984,
            "same_context_pred_std": 0.7676586380046497,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08040898311138153
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1844249345779419
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5154362648129464
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.915474012764295
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9662231980663095,
            "spearman": 0.969199414015625,
            "auroc_top30_worst": 0.9764144761904763,
            "pairwise_seed_ranking": 0.9196,
            "predicted_best_mean_error": 1.8279783728122712,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.08964105272293077,
            "gap_to_oracle": 0.0028054704666138353,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8564022512435913
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0485153335791368
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.342322371673584
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6170351404879393
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5536921262741097,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7672268222173055,
                "rejected_mean_error": 3.109204437255859,
                "gap_rejected_minus_accepted": 1.3419776150385536
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3383561968803406,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6163178348999268,
                "rejected_mean_error": 2.7549230618217884,
                "gap_rejected_minus_accepted": 1.1386052269218616
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9835079908370972,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.342322371673584,
                "rejected_mean_error": 2.460526795768738,
                "gap_rejected_minus_accepted": 1.1182044240951539
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3387452065944672,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0501241531615821,
                "rejected_mean_error": 2.1857970861386082,
                "gap_rejected_minus_accepted": 1.135672932977026
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6160367727279663,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7791646054055956,
                "rejected_mean_error": 3.16371280670166,
                "gap_rejected_minus_accepted": 1.3845482012960644
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.352318048477173,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.628213312217896,
                "rejected_mean_error": 2.7766502698262534,
                "gap_rejected_minus_accepted": 1.1484369576083575
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9973618388175964,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.349019522190094,
                "rejected_mean_error": 2.4862193288803103,
                "gap_rejected_minus_accepted": 1.1371998066902163
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3996368050575256,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0559185450039212,
                "rejected_mean_error": 2.207925069778361,
                "gap_rejected_minus_accepted": 1.1520065247744395
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9583675045012029,
            "spearman": 0.9701299204856938,
            "auroc_top30_bad": 0.9932198095238096,
            "mae": 0.17877953150440007,
            "mse": 0.10407899955670989,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.972,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.6688860103871465,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0608257976770401
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18968155572414397
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47299804685115815
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.8007182960669199
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9510308618829735,
            "spearman": 0.967531949780448,
            "auroc_top30_worst": 0.9770758095238096,
            "pairwise_seed_ranking": 0.912,
            "predicted_best_mean_error": 1.6554034810066223,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07259675335884097,
            "gap_to_oracle": 0.0038747783899306665,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5144825539588929
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7598921268796309
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0173180125236512
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2900561028833328
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.578781580924988,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4938596947987874,
                "rejected_mean_error": 3.7882770233154295,
                "gap_rejected_minus_accepted": 2.294417328516642
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9794114530086517,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2895643019625318,
                "rejected_mean_error": 3.0217413214829785,
                "gap_rejected_minus_accepted": 1.7321770195204467
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4718757271766663,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0173180125236512,
                "rejected_mean_error": 2.429284842777252,
                "gap_rejected_minus_accepted": 1.4119668302536008
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1300058364868164,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7606759895912756,
                "rejected_mean_error": 2.0448614725944454,
                "gap_rejected_minus_accepted": 1.2841854830031698
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.575875449180603,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4953968204392327,
                "rejected_mean_error": 3.821430959701538,
                "gap_rejected_minus_accepted": 2.3260341392623056
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.008574664592743,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.283911642225031,
                "rejected_mean_error": 3.0461679602426197,
                "gap_rejected_minus_accepted": 1.7622563180175888
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4668607711791992,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0139713578224183,
                "rejected_mean_error": 2.4420291109085084,
                "gap_rejected_minus_accepted": 1.42805775308609
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1017585694789886,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7585192455185784,
                "rejected_mean_error": 2.054616824190884,
                "gap_rejected_minus_accepted": 1.2960975786723057
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9878298342941089,
            "spearman": 0.9776614343259256,
            "auroc_top30_bad": 0.9736175898931001,
            "mae": 0.0860753581894096,
            "mse": 0.013158721988269043,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9928571428571429,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6777802517773003,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03336619798626218
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18125520305974144
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5589783887778009
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9154153027704783
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9537486193633775,
            "spearman": 0.9204179017274962,
            "auroc_top30_worst": 0.9393683187560739,
            "pairwise_seed_ranking": 0.8935714285714286,
            "predicted_best_mean_error": 1.618203170810427,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.07949931025505075,
            "gap_to_oracle": 0.003722669397081546,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0411642517362323
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2555988121032715
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4246283483505249
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5258598316283454
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0478233098983765,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5886696196737744,
                "rejected_mean_error": 2.42132648229599,
                "gap_rejected_minus_accepted": 0.8326568626222155
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8831218481063843,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5258598316283454,
                "rejected_mean_error": 2.1101617288589476,
                "gap_rejected_minus_accepted": 0.5843018972306022
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.642710566520691,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4246283483505249,
                "rejected_mean_error": 1.919242263521467,
                "gap_rejected_minus_accepted": 0.4946139151709421
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4565085172653198,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.2555988121032715,
                "rejected_mean_error": 1.8107141372135707,
                "gap_rejected_minus_accepted": 0.5551153251102992
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.064072179794312,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.6080997009125968,
                "rejected_mean_error": 2.5041275024414062,
                "gap_rejected_minus_accepted": 0.8960278015288095
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.911047101020813,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5452246030171712,
                "rejected_mean_error": 2.155136115210397,
                "gap_rejected_minus_accepted": 0.6099115121932257
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6608765125274658,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4466588803700038,
                "rejected_mean_error": 1.9487460817609514,
                "gap_rejected_minus_accepted": 0.5020872013909476
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4831223487854004,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2749897956848144,
                "rejected_mean_error": 1.8386067095256986,
                "gap_rejected_minus_accepted": 0.5636169138408842
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
      "best_epoch": 150,
      "best_calib_loss": 0.0076963333413004875,
      "train_time_sec": 67.04112672805786,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998465037725058,
            "spearman": 0.9992142936133198,
            "auroc_top30_bad": 0.9999574285714286,
            "mae": 0.012897133459057658,
            "mse": 0.0002446982468074463,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6697697319064403,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0004084675647318363
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16852626300901175
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46728248741552236
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7863806047911446
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.999885097476763,
            "spearman": 0.9998925057956977,
            "auroc_top30_worst": 0.9999264761904761,
            "pairwise_seed_ranking": 0.966,
            "predicted_best_mean_error": 1.4522797736227513,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.0760312299728394,
            "gap_to_oracle": 0.0003146517872811838,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5869265820980072
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7975566095352172
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0475831117153167
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2614354280789692
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.294063997268677,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3960914534727733,
                "rejected_mean_error": 2.5832874841690066,
                "gap_rejected_minus_accepted": 1.1871960306962333
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9183952808380127,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2614354280789692,
                "rejected_mean_error": 2.274937941932678,
                "gap_rejected_minus_accepted": 1.0135025138537088
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5288795232772827,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0475831117153167,
                "rejected_mean_error": 1.9820390013694764,
                "gap_rejected_minus_accepted": 0.9344558896541597
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1193718612194061,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7975566095352172,
                "rejected_mean_error": 1.7538958722114564,
                "gap_rejected_minus_accepted": 0.9563392626762391
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3379743814468386,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4065066243873703,
                "rejected_mean_error": 2.624550416469574,
                "gap_rejected_minus_accepted": 1.2180437920822038
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9438980519771576,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2696581125656763,
                "rejected_mean_error": 2.3042696766853332,
                "gap_rejected_minus_accepted": 1.034611564119657
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.545456051826477,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0525066302418709,
                "rejected_mean_error": 2.0041153769493105,
                "gap_rejected_minus_accepted": 0.9516087467074397
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1238516569137573,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7986227031946183,
                "rejected_mean_error": 1.7715404370625814,
                "gap_rejected_minus_accepted": 0.9729177338679631
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9912327069621463,
            "spearman": 0.9905131798296243,
            "auroc_top30_bad": 0.997376,
            "mae": 0.08542992340065539,
            "mse": 0.017312132987904353,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7696459316865639,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06136890459060669
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1743101713180542
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5114762858510017
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9108430227359136
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9830152601100506,
            "spearman": 0.9906862798632193,
            "auroc_top30_worst": 0.9876998095238095,
            "pairwise_seed_ranking": 0.928,
            "predicted_best_mean_error": 1.8264400962591172,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.09117932927608474,
            "gap_to_oracle": 0.001267193913459863,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7616930952072144
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.035042757407213
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3365750951766968
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6126318063054765
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.570083951950074,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7657291866938274,
                "rejected_mean_error": 3.122683156967163,
                "gap_rejected_minus_accepted": 1.3569539702733358
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.321165680885315,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6116913312781709,
                "rejected_mean_error": 2.768773010363594,
                "gap_rejected_minus_accepted": 1.157081679085423
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9456251859664917,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3365750951766968,
                "rejected_mean_error": 2.466274072265625,
                "gap_rejected_minus_accepted": 1.129698977088928
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3781708776950836,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0360746448413252,
                "rejected_mean_error": 2.1904902516714153,
                "gap_rejected_minus_accepted": 1.1544156068300901
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6257406949996946,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7783711483743456,
                "rejected_mean_error": 3.17085391998291,
                "gap_rejected_minus_accepted": 1.3924827716085644
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3403573036193848,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.621558073051473,
                "rejected_mean_error": 2.7964047098916676,
                "gap_rejected_minus_accepted": 1.1748466368401946
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9486223459243774,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3427507815361024,
                "rejected_mean_error": 2.4924880695343017,
                "gap_rejected_minus_accepted": 1.1497372879981993
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3945004343986511,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0370491109197102,
                "rejected_mean_error": 2.214282151849512,
                "gap_rejected_minus_accepted": 1.1772330409298017
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9658108810707684,
            "spearman": 0.9804459859783561,
            "auroc_top30_bad": 0.9988373333333332,
            "mae": 0.14317731182649732,
            "mse": 0.08768812737269739,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6624789366633488,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07318344300985337
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20350049982070922
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4632677452325821
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7775605937163035
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9610687523404077,
            "spearman": 0.9941477625265681,
            "auroc_top30_worst": 0.999872,
            "pairwise_seed_ranking": 0.9308,
            "predicted_best_mean_error": 1.6546491771936416,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07335105717182167,
            "gap_to_oracle": 0.003120474576949972,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5034093980789185
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7506086749908252
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0074867586135865
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2582914819087048
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.577297949790955,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5004364465077717,
                "rejected_mean_error": 3.7290862579345703,
                "gap_rejected_minus_accepted": 2.2286498114267985
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.136000871658325,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2572095081162427,
                "rejected_mean_error": 3.1185989631250646,
                "gap_rejected_minus_accepted": 1.861389455008822
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4925537109375,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0074867586135865,
                "rejected_mean_error": 2.439116096687317,
                "gap_rejected_minus_accepted": 1.4316293380737306
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1277915835380554,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7516124496063866,
                "rejected_mean_error": 2.047889101212663,
                "gap_rejected_minus_accepted": 1.2962766516062767
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.563927674293518,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5019784098201328,
                "rejected_mean_error": 3.7621966552734376,
                "gap_rejected_minus_accepted": 2.260218245453305
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.173202335834503,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.255956850906107,
                "rejected_mean_error": 3.1291448805067272,
                "gap_rejected_minus_accepted": 1.8731880296006203
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4657803177833557,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0020804963111878,
                "rejected_mean_error": 2.453919972419739,
                "gap_rejected_minus_accepted": 1.4518394761085511
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1304064393043518,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7505324180164035,
                "rejected_mean_error": 2.057307573563275,
                "gap_rejected_minus_accepted": 1.3067751555468714
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.992695618762488,
            "spearman": 0.9849113757260967,
            "auroc_top30_bad": 0.9833600583090379,
            "mae": 0.07510379899160138,
            "mse": 0.010045263827746556,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9928571428571429,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7076709444539492,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.03166967555880547
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1819863178048815
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5549980915869985
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9133126078049342
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9765130376072049,
            "spearman": 0.9543828690029397,
            "auroc_top30_worst": 0.9508066083576288,
            "pairwise_seed_ranking": 0.9164285714285715,
            "predicted_best_mean_error": 1.6163627547877175,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.0813397262777602,
            "gap_to_oracle": 0.0018822533743720893,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0225605862481253
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.232416969026838
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4139537276540484
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5242308416820707
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.139912056922913,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5878619001025245,
                "rejected_mean_error": 2.4285959584372385,
                "gap_rejected_minus_accepted": 0.840734058334714
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9293935298919678,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5242308416820707,
                "rejected_mean_error": 2.1150486986977715,
                "gap_rejected_minus_accepted": 0.5908178570157008
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7284332513809204,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4139537276540484,
                "rejected_mean_error": 1.9299168842179435,
                "gap_rejected_minus_accepted": 0.5159631565638951
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5131274461746216,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.232416969026838,
                "rejected_mean_error": 1.8184414182390485,
                "gap_rejected_minus_accepted": 0.5860244492122104
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1134890079498296,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.607087930989644,
                "rejected_mean_error": 2.5132334317479814,
                "gap_rejected_minus_accepted": 0.9061455007583374
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.95962792634964,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5487028451192946,
                "rejected_mean_error": 2.1447013889040267,
                "gap_rejected_minus_accepted": 0.5959985437847322
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7379915118217468,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4397222246442523,
                "rejected_mean_error": 1.955682737486703,
                "gap_rejected_minus_accepted": 0.5159605128424507
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.53900346159935,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2449226209095545,
                "rejected_mean_error": 1.848629101117452,
                "gap_rejected_minus_accepted": 0.6037064802078975
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
      "best_epoch": 122,
      "best_calib_loss": 0.009645607322454453,
      "train_time_sec": 70.2219169139862,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992738611949123,
            "spearman": 0.9984020986384149,
            "auroc_top30_bad": 0.9996135714285714,
            "mae": 0.02816379059597466,
            "mse": 0.0013064002092667225,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.998,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.680414827216533,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.002033130783587694
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1689378303155303
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46741193904802203
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7865899931902687
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9988466373056879,
            "spearman": 0.9988892726115177,
            "auroc_top30_worst": 0.9991710476190476,
            "pairwise_seed_ranking": 0.9656,
            "predicted_best_mean_error": 1.4523338400125503,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07597716358304041,
            "gap_to_oracle": 0.00036871817708017396,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5875514870882035
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7980562215805054
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0480583082675934
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2617370381355286
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.321165490150452,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3962263643741608,
                "rejected_mean_error": 2.5820732860565188,
                "gap_rejected_minus_accepted": 1.185846921682358
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9267126023769379,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2617370381355286,
                "rejected_mean_error": 2.2740331117630004,
                "gap_rejected_minus_accepted": 1.0122960736274718
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5404201745986938,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0480583082675934,
                "rejected_mean_error": 1.9815638048171997,
                "gap_rejected_minus_accepted": 0.9335054965496064
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.11252161860466,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7980562215805054,
                "rejected_mean_error": 1.753729334863027,
                "gap_rejected_minus_accepted": 0.9556731132825216
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3543404579162597,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4066714985171953,
                "rejected_mean_error": 2.6230665493011474,
                "gap_rejected_minus_accepted": 1.216395050783952
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9532201290130615,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.269990709980329,
                "rejected_mean_error": 2.3032718844413758,
                "gap_rejected_minus_accepted": 1.0332811744610468
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5496336817741394,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.05293819886446,
                "rejected_mean_error": 2.003683808326721,
                "gap_rejected_minus_accepted": 0.9507456094622613
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1115091145038605,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7993675047159194,
                "rejected_mean_error": 1.7712921698888142,
                "gap_rejected_minus_accepted": 0.9719246651728948
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9886135546419554,
            "spearman": 0.9848318496402808,
            "auroc_top30_bad": 0.9961379047619048,
            "mae": 0.10592173286419884,
            "mse": 0.020136777243707688,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7666882146999742,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08871031713485718
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.184701389503479
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5124721473813056
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9121194308042526
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9790654839260029,
            "spearman": 0.984327512273608,
            "auroc_top30_worst": 0.984015238095238,
            "pairwise_seed_ranking": 0.9352,
            "predicted_best_mean_error": 1.8262938611507415,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.09132556438446038,
            "gap_to_oracle": 0.0011209588050842267,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7903359065055847
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0407633208311522
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3384547624588012
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6131034267228295
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6175690174102786,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.766096819665697,
                "rejected_mean_error": 3.119374460220337,
                "gap_rejected_minus_accepted": 1.35327764055464
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.34370756149292,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6121137201976878,
                "rejected_mean_error": 2.7675085425757753,
                "gap_rejected_minus_accepted": 1.1553948223780874
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.960082471370697,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3384547624588012,
                "rejected_mean_error": 2.4643944049835205,
                "gap_rejected_minus_accepted": 1.1259396425247192
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3277696073055267,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0422121183559918,
                "rejected_mean_error": 2.1884400604119802,
                "gap_rejected_minus_accepted": 1.1462279420559884
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.650909447669983,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7773317948977152,
                "rejected_mean_error": 3.180208101272583,
                "gap_rejected_minus_accepted": 1.402876306374868
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.371785283088684,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6208299031869613,
                "rejected_mean_error": 2.7985661029815674,
                "gap_rejected_minus_accepted": 1.177736199794606
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9819781184196472,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3438559489250184,
                "rejected_mean_error": 2.4913829021453857,
                "gap_rejected_minus_accepted": 1.1475269532203674
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.342886507511139,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.045734183182792,
                "rejected_mean_error": 2.2113561649373508,
                "gap_rejected_minus_accepted": 1.1656219817545588
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9651121110963892,
            "spearman": 0.965639039805902,
            "auroc_top30_bad": 0.9988091428571428,
            "mae": 0.15727239639878518,
            "mse": 0.08351986624043273,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6400608281944844,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13108753490447997
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21945106747150422
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4820122132539749
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7773501413186391
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9679090074173218,
            "spearman": 0.9930631922324431,
            "auroc_top30_worst": 0.9998780952380953,
            "pairwise_seed_ranking": 0.9252,
            "predicted_best_mean_error": 1.6543784584999084,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07362177586555485,
            "gap_to_oracle": 0.002849755883216787,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5090637092590332
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7559057456942705
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0072484399795532
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.257892536201965
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6060058355331424,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4929258734385173,
                "rejected_mean_error": 3.7966814155578614,
                "gap_rejected_minus_accepted": 2.303755542119344
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.210586726665497,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2568143078204534,
                "rejected_mean_error": 3.1197820387709254,
                "gap_rejected_minus_accepted": 1.862967730950472
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4357572197914124,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0072484399795532,
                "rejected_mean_error": 2.43935441532135,
                "gap_rejected_minus_accepted": 1.4321059753417968
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0489323735237122,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7568986573920082,
                "rejected_mean_error": 2.0461232708637844,
                "gap_rejected_minus_accepted": 1.2892246134717762
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.59113290309906,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4959374499320983,
                "rejected_mean_error": 3.816565294265747,
                "gap_rejected_minus_accepted": 2.3206278443336488
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.279308319091797,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2551605443265987,
                "rejected_mean_error": 3.1315085206712996,
                "gap_rejected_minus_accepted": 1.8763479763447009
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4282278418540955,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0018237957954406,
                "rejected_mean_error": 2.454176672935486,
                "gap_rejected_minus_accepted": 1.4523528771400454
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0449735820293427,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7526133202371144,
                "rejected_mean_error": 2.056606520943463,
                "gap_rejected_minus_accepted": 1.3039932007063486
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9908776454200057,
            "spearman": 0.9888898061731158,
            "auroc_top30_bad": 0.9950655976676385,
            "mae": 0.07757411418730596,
            "mse": 0.011424477821264331,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9785714285714285,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7093429890552336,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.057186285512787954
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18354569332940238
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.556302915087768
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9104476298320862
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9805686358348843,
            "spearman": 0.9832754294250746,
            "auroc_top30_worst": 0.9830320699708455,
            "pairwise_seed_ranking": 0.9128571428571428,
            "predicted_best_mean_error": 1.6166020623275212,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08110041873795648,
            "gap_to_oracle": 0.002121560914175813,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.025762242930276
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2355998039245606
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4032890381131853
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.522359092349098
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0686903476715086,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5876826225765168,
                "rejected_mean_error": 2.4302094561713083,
                "gap_rejected_minus_accepted": 0.8425268335947915
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.936674177646637,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.522359092349098,
                "rejected_mean_error": 2.1206639466966903,
                "gap_rejected_minus_accepted": 0.5983048543475924
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7276448011398315,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4032890381131853,
                "rejected_mean_error": 1.9405815737588066,
                "gap_rejected_minus_accepted": 0.5372925356456213
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.470564216375351,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.2355998039245606,
                "rejected_mean_error": 1.8173804732731411,
                "gap_rejected_minus_accepted": 0.5817806693485805
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.060785460472107,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.6066832126133026,
                "rejected_mean_error": 2.5168758971350536,
                "gap_rejected_minus_accepted": 0.910192684521751
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9525677561759949,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5441233646301997,
                "rejected_mean_error": 2.1584398303713117,
                "gap_rejected_minus_accepted": 0.614316465741112
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.746304452419281,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4259206226893835,
                "rejected_mean_error": 1.969484339441572,
                "gap_rejected_minus_accepted": 0.5435637167521885
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.49227175116539,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2497071198054723,
                "rejected_mean_error": 1.847034268152146,
                "gap_rejected_minus_accepted": 0.5973271483466738
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
      "best_epoch": 137,
      "best_calib_loss": 0.0071179685182869434,
      "train_time_sec": 79.40408515930176,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9993437788676642,
            "spearman": 0.9984721826038391,
            "auroc_top30_bad": 0.9996710476190477,
            "mae": 0.028166290390694484,
            "mse": 0.0015237037454402787,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6858113319578842,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0014414685107767581
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16897955039590598
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4674343977443874
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7865154586151242
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9989933307679096,
            "spearman": 0.9990271622890631,
            "auroc_top30_worst": 0.999476,
            "pairwise_seed_ranking": 0.9714,
            "predicted_best_mean_error": 1.4524240966439248,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07588690695166589,
            "gap_to_oracle": 0.00045897480845469296,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5875566022396088
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7980410985946655
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0478645364761352
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2616746458689372
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3286930561065673,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3963400390677982,
                "rejected_mean_error": 2.5810502138137816,
                "gap_rejected_minus_accepted": 1.1847101747459834
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9381438493728638,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2616746458689372,
                "rejected_mean_error": 2.2742202885627747,
                "gap_rejected_minus_accepted": 1.0125456426938375
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5361943244934082,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0478645364761352,
                "rejected_mean_error": 1.981757576608658,
                "gap_rejected_minus_accepted": 0.9338930401325227
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.109336793422699,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7980410985946655,
                "rejected_mean_error": 1.7537343758583068,
                "gap_rejected_minus_accepted": 0.9556932772636413
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.35820791721344,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4070181392629941,
                "rejected_mean_error": 2.6199467825889586,
                "gap_rejected_minus_accepted": 1.2129286433259645
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9802448749542236,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2698635777235032,
                "rejected_mean_error": 2.303653281211853,
                "gap_rejected_minus_accepted": 1.0337897034883499
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5578078627586365,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0529582284092902,
                "rejected_mean_error": 2.003663778781891,
                "gap_rejected_minus_accepted": 0.9507055503726007
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1159079670906067,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7988356105089187,
                "rejected_mean_error": 1.7714694679578145,
                "gap_rejected_minus_accepted": 0.9726338574488957
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9910694031420146,
            "spearman": 0.9866657446364548,
            "auroc_top30_bad": 0.9966285714285714,
            "mae": 0.0875652285144466,
            "mse": 0.014923118775612964,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.794752256082649,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07882329887151718
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1836121881008148
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5125988680958747
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9125499749581019
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9868914490151728,
            "spearman": 0.9890719858380712,
            "auroc_top30_worst": 0.9860998095238096,
            "pairwise_seed_ranking": 0.9352,
            "predicted_best_mean_error": 1.8261956813335418,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.0914237442016601,
            "gap_to_oracle": 0.0010227789878844984,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7592590532302856
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0392908262900817
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.337459508705139
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6108311510035225
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6950613498687743,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7641705507702297,
                "rejected_mean_error": 3.136710880279541,
                "gap_rejected_minus_accepted": 1.3725403295093115
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3907853960990906,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6100325646751592,
                "rejected_mean_error": 2.7737387110250067,
                "gap_rejected_minus_accepted": 1.1637061463498475
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.972410261631012,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.337459508705139,
                "rejected_mean_error": 2.4653896587371826,
                "gap_rejected_minus_accepted": 1.1279301500320436
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3763573467731476,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0402651042603075,
                "rejected_mean_error": 2.1890904503927158,
                "gap_rejected_minus_accepted": 1.1488253461324083
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.76131329536438,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7754623548189798,
                "rejected_mean_error": 3.1970330619812013,
                "gap_rejected_minus_accepted": 1.4215707071622214
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.406303286552429,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.619432793262808,
                "rejected_mean_error": 2.802713080058022,
                "gap_rejected_minus_accepted": 1.1832802867952141
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9976457357406616,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.343865975856781,
                "rejected_mean_error": 2.491372875213623,
                "gap_rejected_minus_accepted": 1.147506899356842
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.390986979007721,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.045734183182792,
                "rejected_mean_error": 2.2113561649373508,
                "gap_rejected_minus_accepted": 1.1656219817545588
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9710590270227621,
            "spearman": 0.9671207805721087,
            "auroc_top30_bad": 0.998472380952381,
            "mae": 0.13907663819176158,
            "mse": 0.06054952832272388,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6820996630053805,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12370531088113784
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21256837317943572
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.48242424899339675
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.777301586898168
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9753583420212977,
            "spearman": 0.9951036036503064,
            "auroc_top30_worst": 0.9994544761904762,
            "pairwise_seed_ranking": 0.9396,
            "predicted_best_mean_error": 1.654024881720543,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07397535264492028,
            "gap_to_oracle": 0.002496179103851359,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5078069477081298
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7522603367001582
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0065850135803223
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2580441986319861
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.831603503227234,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4893963072035048,
                "rejected_mean_error": 3.8284475116729735,
                "gap_rejected_minus_accepted": 2.3390512044694685
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.361152231693268,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2569661321100583,
                "rejected_mean_error": 3.1193275360253674,
                "gap_rejected_minus_accepted": 1.8623614039153091
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4242583513259888,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0065850135803223,
                "rejected_mean_error": 2.440017841720581,
                "gap_rejected_minus_accepted": 1.4334328281402586
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0571723580360413,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7536278203272591,
                "rejected_mean_error": 2.047215877055104,
                "gap_rejected_minus_accepted": 1.293588056727845
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.833404207229614,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4903555199835035,
                "rejected_mean_error": 3.866802663803101,
                "gap_rejected_minus_accepted": 2.3764471438195973
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.4419326186180115,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2561855185478128,
                "rejected_mean_error": 3.1284661368718223,
                "gap_rejected_minus_accepted": 1.8722806183240095
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4000772833824158,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0019959034919739,
                "rejected_mean_error": 2.454004565238953,
                "gap_rejected_minus_accepted": 1.452008661746979
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0493818521499634,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7496174431982494,
                "rejected_mean_error": 2.0576158271116367,
                "gap_rejected_minus_accepted": 1.3079983839133873
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9883003899343579,
            "spearman": 0.9862059202990935,
            "auroc_top30_bad": 0.9937779397473275,
            "mae": 0.07365236544461563,
            "mse": 0.012743715840356811,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9857142857142858,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6935415703586619,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.054592608234712056
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19565644634621485
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.557563833466598
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9106489049536841
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9830106328642072,
            "spearman": 0.9810587485163963,
            "auroc_top30_worst": 0.9814577259475219,
            "pairwise_seed_ranking": 0.9257142857142857,
            "predicted_best_mean_error": 1.6160480635506767,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08165441751480107,
            "gap_to_oracle": 0.0015675621373312243,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.02702545608793
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.236046246119908
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4026559696878707
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5227800153550648
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0204612731933596,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5882062128611973,
                "rejected_mean_error": 2.4254971436091832,
                "gap_rejected_minus_accepted": 0.8372909307479859
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8598338663578033,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5227800153550648,
                "rejected_mean_error": 2.1194011776787893,
                "gap_rejected_minus_accepted": 0.5966211623237245
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.685859203338623,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4026559696878707,
                "rejected_mean_error": 1.9412146421841212,
                "gap_rejected_minus_accepted": 0.5385586724962506
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.376622349023819,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.236046246119908,
                "rejected_mean_error": 1.8172316592080253,
                "gap_rejected_minus_accepted": 0.5811854130881173
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.031954145431519,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.607087930989644,
                "rejected_mean_error": 2.5132334317479814,
                "gap_rejected_minus_accepted": 0.9061455007583374
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8911941647529602,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.543989830925351,
                "rejected_mean_error": 2.1588404314858574,
                "gap_rejected_minus_accepted": 0.6148506005605063
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.699047327041626,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.424339531149183,
                "rejected_mean_error": 1.9710654309817723,
                "gap_rejected_minus_accepted": 0.5467258998325892
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4266703426837921,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2439550808497837,
                "rejected_mean_error": 1.848951614470709,
                "gap_rejected_minus_accepted": 0.6049965336209253
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
      "best_epoch": 96,
      "best_calib_loss": 0.008899271488189697,
      "train_time_sec": 54.943944215774536,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997027932511983,
            "spearman": 0.99898280712288,
            "auroc_top30_bad": 0.9998369047619048,
            "mae": 0.021494079978340595,
            "mse": 0.0008470423710634854,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6784286929950326,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0008857977651059628
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16871126659959554
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46730505919381976
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7864327897384763
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9995738440685104,
            "spearman": 0.9995265935010411,
            "auroc_top30_worst": 0.999684761904762,
            "pairwise_seed_ranking": 0.9662,
            "predicted_best_mean_error": 1.4523359062969685,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07597509729862217,
            "gap_to_oracle": 0.00037078446149840794,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5871206105947494
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7976859168052673
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0477342814445496
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2615319335619608
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.313230276107788,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3961402941544852,
                "rejected_mean_error": 2.5828479180336,
                "gap_rejected_minus_accepted": 1.1867076238791148
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9392460882663727,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2615319335619608,
                "rejected_mean_error": 2.274648425483704,
                "gap_rejected_minus_accepted": 1.013116491921743
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5380609631538391,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0477342814445496,
                "rejected_mean_error": 1.9818878316402435,
                "gap_rejected_minus_accepted": 0.9341535501956939
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.121771901845932,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7976859168052673,
                "rejected_mean_error": 1.7538527697881063,
                "gap_rejected_minus_accepted": 0.956166852982839
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3467320442199706,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.40653809087144,
                "rejected_mean_error": 2.6242672181129456,
                "gap_rejected_minus_accepted": 1.2177291272415056
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9591396749019623,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.269751803278923,
                "rejected_mean_error": 2.303988604545593,
                "gap_rejected_minus_accepted": 1.03423680126667
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5566090941429138,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0527673235535622,
                "rejected_mean_error": 2.003854683637619,
                "gap_rejected_minus_accepted": 0.9510873600840568
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1253263652324677,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7986502867937088,
                "rejected_mean_error": 1.7715312425295513,
                "gap_rejected_minus_accepted": 0.9728809557358425
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9895963183998528,
            "spearman": 0.9861999192735491,
            "auroc_top30_bad": 0.9950567619047619,
            "mae": 0.09826460603047744,
            "mse": 0.01908234884593866,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7678834641375042,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07395782405138016
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18469036338329314
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5116311582684517
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.913296943672498
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9809012804425422,
            "spearman": 0.9843197339646298,
            "auroc_top30_worst": 0.9793615238095238,
            "pairwise_seed_ranking": 0.9384,
            "predicted_best_mean_error": 1.8261874482631684,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.09143197727203356,
            "gap_to_oracle": 0.001014545917511045,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7628968334197999
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0360630448812094
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3409913648605347
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.614978314589844
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.59921042919159,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.765065157254537,
                "rejected_mean_error": 3.1286594219207764,
                "gap_rejected_minus_accepted": 1.3635942646662393
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.347798228263855,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6139809445357756,
                "rejected_mean_error": 2.7619188007074422,
                "gap_rejected_minus_accepted": 1.1479378561716667
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9271793365478516,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3409913648605347,
                "rejected_mean_error": 2.461857802581787,
                "gap_rejected_minus_accepted": 1.1208664377212523
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3412044942378998,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0370686644563278,
                "rejected_mean_error": 2.1901582045641628,
                "gap_rejected_minus_accepted": 1.153089540107835
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.651768660545349,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7773297497961256,
                "rejected_mean_error": 3.1802265071868896,
                "gap_rejected_minus_accepted": 1.402896757390764
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3732864260673523,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6252276180262235,
                "rejected_mean_error": 2.785512568458678,
                "gap_rejected_minus_accepted": 1.1602849504324546
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9276504516601562,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.347683503627777,
                "rejected_mean_error": 2.487555347442627,
                "gap_rejected_minus_accepted": 1.13987184381485
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3624645471572876,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0394421352280512,
                "rejected_mean_error": 2.2134759457991087,
                "gap_rejected_minus_accepted": 1.1740338105710575
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.970313971793286,
            "spearman": 0.9700175876798877,
            "auroc_top30_bad": 0.9982872380952381,
            "mae": 0.14846405657943687,
            "mse": 0.07200220168529196,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 0.992,
            "same_context_pred_std": 0.6529863177302816,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.13181668108701705
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21671361269950867
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4732007607340813
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7771316112359364
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9704630935243096,
            "spearman": 0.9913609775110257,
            "auroc_top30_worst": 0.999527619047619,
            "pairwise_seed_ranking": 0.9292,
            "predicted_best_mean_error": 1.6537368404865265,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07426339387893677,
            "gap_to_oracle": 0.0022081378698348697,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5164449501037598
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7559554154674212
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0084297342300415
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2585146348359488
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.597727060317993,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4937703853183322,
                "rejected_mean_error": 3.7890808086395262,
                "gap_rejected_minus_accepted": 2.295310423321194
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.238121211528778,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2574875619393657,
                "rejected_mean_error": 3.1177665783574406,
                "gap_rejected_minus_accepted": 1.860279016418075
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4220398664474487,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0084297342300415,
                "rejected_mean_error": 2.4381731210708617,
                "gap_rejected_minus_accepted": 1.4297433868408203
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0409405529499054,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7569786095009825,
                "rejected_mean_error": 2.046096563275621,
                "gap_rejected_minus_accepted": 1.2891179537746387
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.586452102661133,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4958943417337205,
                "rejected_mean_error": 3.8169532680511473,
                "gap_rejected_minus_accepted": 2.321058926317427
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3006264567375183,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.256442694421758,
                "rejected_mean_error": 3.1277027735634455,
                "gap_rejected_minus_accepted": 1.8712600791416876
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4064194560050964,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.003122019290924,
                "rejected_mean_error": 2.4528784494400027,
                "gap_rejected_minus_accepted": 1.4497564301490786
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0218655467033386,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7537460582596915,
                "rejected_mean_error": 2.0562249033208837,
                "gap_rejected_minus_accepted": 1.3024788450611922
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9894628378011602,
            "spearman": 0.9841947713546568,
            "auroc_top30_bad": 0.9877478134110786,
            "mae": 0.07838334155914188,
            "mse": 0.01252208174196546,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9714285714285714,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7006453971785226,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.057685211939471105
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1803416566337858
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5576164750967707
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9117117568140938
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9657903973487025,
            "spearman": 0.9588938986172858,
            "auroc_top30_worst": 0.9657434402332362,
            "pairwise_seed_ranking": 0.9292857142857143,
            "predicted_best_mean_error": 1.616401707274573,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08130077379090461,
            "gap_to_oracle": 0.0019212058612276817,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0420879193714687
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.239697470664978
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.409428334236145
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5268297415687924
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.09050567150116,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5885268099724301,
                "rejected_mean_error": 2.422611769608089,
                "gap_rejected_minus_accepted": 0.834084959635659
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9600960314273834,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5268297415687924,
                "rejected_mean_error": 2.107251999037606,
                "gap_rejected_minus_accepted": 0.5804222574688138
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.724612832069397,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.409428334236145,
                "rejected_mean_error": 1.9344422776358468,
                "gap_rejected_minus_accepted": 0.5250139433997016
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.476954847574234,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.239697470664978,
                "rejected_mean_error": 1.8160145843596684,
                "gap_rejected_minus_accepted": 0.5763171136946905
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.07787139415741,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.6080997009125968,
                "rejected_mean_error": 2.5041275024414062,
                "gap_rejected_minus_accepted": 0.8960278015288095
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9890332520008087,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5486397924877349,
                "rejected_mean_error": 2.144890546798706,
                "gap_rejected_minus_accepted": 0.5962507543109712
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7403359413146973,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4302681531224932,
                "rejected_mean_error": 1.965136809008462,
                "gap_rejected_minus_accepted": 0.5348686558859688
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4881200790405273,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.253811628477914,
                "rejected_mean_error": 1.8456660985946656,
                "gap_rejected_minus_accepted": 0.5918544701167516
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
      "best_calib_loss": 0.007749421522021294,
      "train_time_sec": 72.4549400806427,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996338246776221,
            "spearman": 0.9990242461719963,
            "auroc_top30_bad": 0.9998332857142856,
            "mae": 0.017391160318825222,
            "mse": 0.0005957730689787257,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.67085981093947,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0007904290817677974
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16871318751424552
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46734690565988424
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.786426911401252
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9994104616860736,
            "spearman": 0.999414225496541,
            "auroc_top30_worst": 0.9997297142857143,
            "pairwise_seed_ranking": 0.9702,
            "predicted_best_mean_error": 1.4522583620548248,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07605264154076585,
            "gap_to_oracle": 0.000293240219354729,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5872147784233094
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7979338399887085
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0477632600784301
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2614874346733094
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3049857616424565,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3961684013737572,
                "rejected_mean_error": 2.58259495306015,
                "gap_rejected_minus_accepted": 1.186426551686393
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9281084537506104,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2614874346733094,
                "rejected_mean_error": 2.2747819221496584,
                "gap_rejected_minus_accepted": 1.013294487476349
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5270816087722778,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0477632600784301,
                "rejected_mean_error": 1.981858853006363,
                "gap_rejected_minus_accepted": 0.9340955929279329
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1136829555034637,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7979338399887085,
                "rejected_mean_error": 1.7537701287269591,
                "gap_rejected_minus_accepted": 0.9558362887382507
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3432910680770873,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.406639346447256,
                "rejected_mean_error": 2.623355917930603,
                "gap_rejected_minus_accepted": 1.2167165714833472
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9453247785568237,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2697314858833948,
                "rejected_mean_error": 2.3040495567321777,
                "gap_rejected_minus_accepted": 1.034318070848783
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.54061621427536,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0526886113286018,
                "rejected_mean_error": 2.003933395862579,
                "gap_rejected_minus_accepted": 0.9512447845339773
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.122105985879898,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.798891097664833,
                "rejected_mean_error": 1.7714509722391765,
                "gap_rejected_minus_accepted": 0.9725598745743435
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.991184704897436,
            "spearman": 0.9884321631875428,
            "auroc_top30_bad": 0.9963222857142857,
            "mae": 0.09299055708407232,
            "mse": 0.016480150095579602,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.769333753946351,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.061368368446826936
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1850120335817337
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.512722320663929
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9117169244845709
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9841779617368128,
            "spearman": 0.9887404922499151,
            "auroc_top30_worst": 0.988583619047619,
            "pairwise_seed_ranking": 0.9368,
            "predicted_best_mean_error": 1.8259653265476228,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.09165409898757915,
            "gap_to_oracle": 0.0007924242019654582,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7647361907958984
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0370364406934152
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3387281784057616
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6123676194565129
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6411190748214723,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7641662318971423,
                "rejected_mean_error": 3.136749750137329,
                "gap_rejected_minus_accepted": 1.3725835182401869
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3379204869270325,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6116830965498086,
                "rejected_mean_error": 2.7687976619306083,
                "gap_rejected_minus_accepted": 1.1571145653807997
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9409071207046509,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3387281784057616,
                "rejected_mean_error": 2.46412098903656,
                "gap_rejected_minus_accepted": 1.1253928106307984
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2956324219703674,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.038265192851472,
                "rejected_mean_error": 2.1897585104471085,
                "gap_rejected_minus_accepted": 1.1514933175956366
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6900632858276365,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.775963916513655,
                "rejected_mean_error": 3.192519006729126,
                "gap_rejected_minus_accepted": 1.416555090215471
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3575470447540283,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.62128232347774,
                "rejected_mean_error": 2.797223204658145,
                "gap_rejected_minus_accepted": 1.1759408811804049
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9410490989685059,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3457985854148864,
                "rejected_mean_error": 2.4894402656555177,
                "gap_rejected_minus_accepted": 1.1436416802406313
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3158282935619354,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0424709424139962,
                "rejected_mean_error": 2.2124555455172126,
                "gap_rejected_minus_accepted": 1.1699846031032164
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9709665291914424,
            "spearman": 0.9706219458359173,
            "auroc_top30_bad": 0.9984769523809524,
            "mae": 0.14303199184160725,
            "mse": 0.07005250062075999,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6541759141379073,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11772061848640442
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20995218234062193
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.47852200142145157
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7782407380898794
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9697222716050402,
            "spearman": 0.9933845052060835,
            "auroc_top30_worst": 0.9997287619047619,
            "pairwise_seed_ranking": 0.934,
            "predicted_best_mean_error": 1.654025365948677,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07397486841678624,
            "gap_to_oracle": 0.0024966633319853937,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5205562653541564
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.752989119826219
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0084091381072997
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2578827099505263
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6702795505523684,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4923442679511176,
                "rejected_mean_error": 3.801915864944458,
                "gap_rejected_minus_accepted": 2.30957159699334
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.248018264770508,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2568223669791043,
                "rejected_mean_error": 3.119757912791194,
                "gap_rejected_minus_accepted": 1.8629355458120898
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.43413245677948,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0084091381072997,
                "rejected_mean_error": 2.4381937171936037,
                "gap_rejected_minus_accepted": 1.429784579086304
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0364665389060974,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7540584014246638,
                "rejected_mean_error": 2.047072043668244,
                "gap_rejected_minus_accepted": 1.2930136422435803
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6589618921279907,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.494221980571747,
                "rejected_mean_error": 3.8320045185089113,
                "gap_rejected_minus_accepted": 2.3377825379371644
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3224847316741943,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2551605443265987,
                "rejected_mean_error": 3.1315085206712996,
                "gap_rejected_minus_accepted": 1.8763479763447009
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4125548601150513,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.003815800189972,
                "rejected_mean_error": 2.4521846685409545,
                "gap_rejected_minus_accepted": 1.4483688683509826
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.051317572593689,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7535813952249194,
                "rejected_mean_error": 2.056280378033133,
                "gap_rejected_minus_accepted": 1.3026989828082134
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9894923542416576,
            "spearman": 0.9861897073721245,
            "auroc_top30_bad": 0.9913678328474248,
            "mae": 0.07676896434573248,
            "mse": 0.012719202895659273,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9857142857142858,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6976339200293131,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06340232821447508
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18442725049597877
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5559588523847716
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9123153135606221
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9806647163861962,
            "spearman": 0.9710157775832194,
            "auroc_top30_worst": 0.9708260447035957,
            "pairwise_seed_ranking": 0.9328571428571428,
            "predicted_best_mean_error": 1.6154078202588218,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08229466080665593,
            "gap_to_oracle": 0.0009273188454763659,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0222012724195209
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2325692728587558
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4076539322308133
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5234742961611067
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0873657464981084,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5878619001025245,
                "rejected_mean_error": 2.4285959584372385,
                "gap_rejected_minus_accepted": 0.840734058334714
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.93325537443161,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5234742961611067,
                "rejected_mean_error": 2.1173183352606637,
                "gap_rejected_minus_accepted": 0.593844039099557
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7022374868392944,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4076539322308133,
                "rejected_mean_error": 1.9362166796411786,
                "gap_rejected_minus_accepted": 0.5285627474103654
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4648741483688354,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.2325692728587558,
                "rejected_mean_error": 1.818390650295076,
                "gap_rejected_minus_accepted": 0.5858213774363201
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0826962947845464,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.607087930989644,
                "rejected_mean_error": 2.5132334317479814,
                "gap_rejected_minus_accepted": 0.9061455007583374
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9567607641220093,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5445269368943715,
                "rejected_mean_error": 2.157229113578796,
                "gap_rejected_minus_accepted": 0.6127021766844247
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.728107511997223,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4306247557912555,
                "rejected_mean_error": 1.9647802063397,
                "gap_rejected_minus_accepted": 0.5341554505484445
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4812391102313995,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2438759769712175,
                "rejected_mean_error": 1.848977982430231,
                "gap_rejected_minus_accepted": 0.6051020054590135
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
      "best_epoch": 142,
      "best_calib_loss": 0.009561445564031601,
      "train_time_sec": 72.78732323646545,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999678264787227,
            "spearman": 0.9990424558352898,
            "auroc_top30_bad": 0.9998699047619047,
            "mae": 0.01558220590081155,
            "mse": 0.0004923465253284209,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6728779923196079,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010294303111732005
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1686493646964431
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4672896345131099
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7864465018267432
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9995484284596649,
            "spearman": 0.9995627151104982,
            "auroc_top30_worst": 0.9995245714285714,
            "pairwise_seed_ranking": 0.9696,
            "predicted_best_mean_error": 1.4521997518241405,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07611125177145017,
            "gap_to_oracle": 0.00023462998867040952,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5869690697193146
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7977051040649414
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.04774537525177
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2615677167892456
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.298598551750183,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3961432667573292,
                "rejected_mean_error": 2.582821164608002,
                "gap_rejected_minus_accepted": 1.1866778978506727
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9185550212860107,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2615677167892456,
                "rejected_mean_error": 2.2745410758018494,
                "gap_rejected_minus_accepted": 1.0129733590126038
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5232080221176147,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.04774537525177,
                "rejected_mean_error": 1.981876737833023,
                "gap_rejected_minus_accepted": 0.9341313625812531
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1180780529975891,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7977051040649414,
                "rejected_mean_error": 1.7538463740348815,
                "gap_rejected_minus_accepted": 0.9561412699699401
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3397406339645386,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.406659006708198,
                "rejected_mean_error": 2.623178975582123,
                "gap_rejected_minus_accepted": 1.2165199688739248
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9457551836967468,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.269755348086357,
                "rejected_mean_error": 2.303977970123291,
                "gap_rejected_minus_accepted": 1.0342226220369342
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5369197130203247,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0526872175335884,
                "rejected_mean_error": 2.0039347896575928,
                "gap_rejected_minus_accepted": 0.9512475721240043
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.12531179189682,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7987054044008255,
                "rejected_mean_error": 1.7715128699938456,
                "gap_rejected_minus_accepted": 0.9728074655930201
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9885617368412954,
            "spearman": 0.985497534476795,
            "auroc_top30_bad": 0.996567619047619,
            "mae": 0.10093359192820399,
            "mse": 0.021193204449871453,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7647456173737083,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09264333695173263
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1909881840467453
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5116752296566963
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9118089070717493
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.981587355835521,
            "spearman": 0.9896450616608395,
            "auroc_top30_worst": 0.9883611428571428,
            "pairwise_seed_ranking": 0.942,
            "predicted_best_mean_error": 1.8262205940485001,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.0913988314867018,
            "gap_to_oracle": 0.0010476917028428012,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7695942888259888
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0353096379683568
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3382496082305908
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.611844797251321
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.586567783355713,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7645112941530017,
                "rejected_mean_error": 3.1336441898345946,
                "gap_rejected_minus_accepted": 1.369132895681593
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3207335472106934,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6109245239479693,
                "rejected_mean_error": 2.77106853262685,
                "gap_rejected_minus_accepted": 1.1601440086788806
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9636372923851013,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3382496082305908,
                "rejected_mean_error": 2.464599559211731,
                "gap_rejected_minus_accepted": 1.12634995098114
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.394947499036789,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.036618022872998,
                "rejected_mean_error": 2.190308739052511,
                "gap_rejected_minus_accepted": 1.1536907161795131
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6315820455551147,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.775963916513655,
                "rejected_mean_error": 3.192519006729126,
                "gap_rejected_minus_accepted": 1.416555090215471
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3401885628700256,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6216792993367037,
                "rejected_mean_error": 2.7960448794894748,
                "gap_rejected_minus_accepted": 1.174365580152771
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9686877727508545,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3438559489250184,
                "rejected_mean_error": 2.4913829021453857,
                "gap_rejected_minus_accepted": 1.1475269532203674
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.394244760274887,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.038591860778748,
                "rejected_mean_error": 2.213762401897002,
                "gap_rejected_minus_accepted": 1.1751705411182538
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9670462272431634,
            "spearman": 0.9707810452060796,
            "auroc_top30_bad": 0.9987207619047618,
            "mae": 0.15159937768423948,
            "mse": 0.08241026837571742,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6432349934534147,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.11470712167024612
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20729843306541443
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.48157727696895597
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7775440818627676
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9702695313943184,
            "spearman": 0.9949189394681214,
            "auroc_top30_worst": 0.999640380952381,
            "pairwise_seed_ranking": 0.9364,
            "predicted_best_mean_error": 1.6541537486314775,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07384648573398578,
            "gap_to_oracle": 0.002625046014785859,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5040240683555604
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.75176463696437
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.007517205429077
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2582232944492593
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.571020793914795,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4930742852952745,
                "rejected_mean_error": 3.7953457088470457,
                "gap_rejected_minus_accepted": 2.302271423551771
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.192497193813324,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2571445547020423,
                "rejected_mean_error": 3.1187934083298754,
                "gap_rejected_minus_accepted": 1.861648853627833
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4481452703475952,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.007517205429077,
                "rejected_mean_error": 2.439085649871826,
                "gap_rejected_minus_accepted": 1.431568444442749
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.065712809562683,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7530230811228767,
                "rejected_mean_error": 2.0474178870561413,
                "gap_rejected_minus_accepted": 1.2943948059332646
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5652992725372314,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4936056844393413,
                "rejected_mean_error": 3.8375511837005614,
                "gap_rejected_minus_accepted": 2.34394549926122
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2401965260505676,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2555086622263658,
                "rejected_mean_error": 3.130475218333895,
                "gap_rejected_minus_accepted": 1.8749665561075293
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4302031993865967,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0016037220954894,
                "rejected_mean_error": 2.454396746635437,
                "gap_rejected_minus_accepted": 1.4527930245399476
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.063757985830307,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.750454190231505,
                "rejected_mean_error": 2.057333928378508,
                "gap_rejected_minus_accepted": 1.3068797381470032
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9880820079637314,
            "spearman": 0.9884385897615474,
            "auroc_top30_bad": 0.9957871720116618,
            "mae": 0.0698656065822191,
            "mse": 0.013082274820065526,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9714285714285714,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6842035596262114,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.060106178373098375
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1928542313831193
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5558147728017399
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9097128445477712
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9834583844216138,
            "spearman": 0.9864381180952846,
            "auroc_top30_worst": 0.9902721088435374,
            "pairwise_seed_ranking": 0.9321428571428572,
            "predicted_best_mean_error": 1.6160639379705701,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08163854309490759,
            "gap_to_oracle": 0.0015834365572247044,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0224062510899135
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2318747391019549
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4052703326089042
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.521295644896371
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.03724889755249,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5881528275353567,
                "rejected_mean_error": 2.425977611541748,
                "gap_rejected_minus_accepted": 0.8378247840063913
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8539682626724243,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.521295644896371,
                "rejected_mean_error": 2.1238542890548704,
                "gap_rejected_minus_accepted": 0.6025586441584994
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.692848265171051,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4052703326089042,
                "rejected_mean_error": 1.9386002792630876,
                "gap_rejected_minus_accepted": 0.5333299466541834
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4650379717350006,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.2318747391019549,
                "rejected_mean_error": 1.818622161547343,
                "gap_rejected_minus_accepted": 0.5867474224453881
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0433656692504885,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.607087930989644,
                "rejected_mean_error": 2.5132334317479814,
                "gap_rejected_minus_accepted": 0.9061455007583374
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8886711597442627,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5436638264429001,
                "rejected_mean_error": 2.1598184449332103,
                "gap_rejected_minus_accepted": 0.6161546184903102
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7045810222625732,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.427350732258388,
                "rejected_mean_error": 1.9680542298725674,
                "gap_rejected_minus_accepted": 0.5407034976141794
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4874825477600098,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2438759769712175,
                "rejected_mean_error": 1.848977982430231,
                "gap_rejected_minus_accepted": 0.6051020054590135
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
      "best_epoch": 146,
      "best_calib_loss": 0.00832432135939598,
      "train_time_sec": 79.74779558181763,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9984995565089327,
            "spearman": 0.9976984137561827,
            "auroc_top30_bad": 0.9992447142857143,
            "mae": 0.04300423800492499,
            "mse": 0.003343732512215852,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.692414434513747,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0032461859695613383
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16909600119441748
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.4678144591085613
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7868804992988706
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9978133484508839,
            "spearman": 0.9977493673658668,
            "auroc_top30_worst": 0.9988868571428572,
            "pairwise_seed_ranking": 0.9699,
            "predicted_best_mean_error": 1.4524020492434502,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07590895435214051,
            "gap_to_oracle": 0.00043692740798007,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5878886671066285
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.798390629863739
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0486131103992462
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2617841643015544
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3666809558868414,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3962918128172557,
                "rejected_mean_error": 2.5814842500686646,
                "gap_rejected_minus_accepted": 1.1851924372514089
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9633696973323822,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2617841643015544,
                "rejected_mean_error": 2.273891733264923,
                "gap_rejected_minus_accepted": 1.0121075689633685
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5450668334960938,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0486131103992462,
                "rejected_mean_error": 1.981009002685547,
                "gap_rejected_minus_accepted": 0.9323958922863007
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1371637880802155,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.798390629863739,
                "rejected_mean_error": 1.7536178654352823,
                "gap_rejected_minus_accepted": 0.9552272355715433
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4143063068389896,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4066008444958262,
                "rejected_mean_error": 2.623702435493469,
                "gap_rejected_minus_accepted": 1.2171015909976428
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.995654135942459,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2699081510305406,
                "rejected_mean_error": 2.303519561290741,
                "gap_rejected_minus_accepted": 1.0336114102602005
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5597350001335144,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0534616869091988,
                "rejected_mean_error": 2.0031603202819825,
                "gap_rejected_minus_accepted": 0.9496986333727837
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1446243524551392,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7989214321374893,
                "rejected_mean_error": 1.771440860748291,
                "gap_rejected_minus_accepted": 0.9725194286108017
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9895990581432599,
            "spearman": 0.9843018292178991,
            "auroc_top30_bad": 0.9963687619047619,
            "mae": 0.09787268324387405,
            "mse": 0.01750413866089674,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.8023837604295474,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10103098499774933
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19441183547973634
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5124582159161568
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9113890086571376
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9848530506167099,
            "spearman": 0.9917593362939754,
            "auroc_top30_worst": 0.993088,
            "pairwise_seed_ranking": 0.9332,
            "predicted_best_mean_error": 1.826310798406601,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.091308627128601,
            "gap_to_oracle": 0.0011378960609436106,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7702938776016235
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.042428575265102
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3359535045623778
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6098862580144837
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7219391345977786,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7643946903016832,
                "rejected_mean_error": 3.13469362449646,
                "gap_rejected_minus_accepted": 1.3702989341947767
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.445988118648529,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.609049178874607,
                "rejected_mean_error": 2.7766825848113235,
                "gap_rejected_minus_accepted": 1.1676334059367164
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.0115801095962524,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3359535045623778,
                "rejected_mean_error": 2.466895662879944,
                "gap_rejected_minus_accepted": 1.130942158317566
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4067368507385254,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0433082770996582,
                "rejected_mean_error": 2.1880738942574793,
                "gap_rejected_minus_accepted": 1.144765617157821
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7529234170913695,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.775963916513655,
                "rejected_mean_error": 3.192519006729126,
                "gap_rejected_minus_accepted": 1.416555090215471
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.4845981001853943,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6180862280774244,
                "rejected_mean_error": 2.80671002751305,
                "gap_rejected_minus_accepted": 1.1886237994356255
              },
              {
                "reject_rate": 0.5,
                "threshold": 2.0299875736236572,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3423662991523744,
                "rejected_mean_error": 2.4928725519180297,
                "gap_rejected_minus_accepted": 1.1505062527656553
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.413394570350647,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.049026976502131,
                "rejected_mean_error": 2.2102468281506216,
                "gap_rejected_minus_accepted": 1.1612198516484906
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9699431924710795,
            "spearman": 0.9634803129910101,
            "auroc_top30_bad": 0.9981325714285715,
            "mae": 0.15347103472468515,
            "mse": 0.06030872585775851,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6908229751337935,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12905347019433974
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21969294385910035
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.48255890852212907
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7781523441155751
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9757677468120955,
            "spearman": 0.9924076515888971,
            "auroc_top30_worst": 0.9992198095238095,
            "pairwise_seed_ranking": 0.9248,
            "predicted_best_mean_error": 1.6544169956445693,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.0735832387208939,
            "gap_to_oracle": 0.002888293027877742,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5072554292678833
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7533301105483984
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0085906717300415
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2579731407450205
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8745919466018677,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.49061850505405,
                "rejected_mean_error": 3.8174477310180666,
                "gap_rejected_minus_accepted": 2.3268292259640164
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.390883982181549,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2570677238696413,
                "rejected_mean_error": 3.1190234098952416,
                "gap_rejected_minus_accepted": 1.8619556860256004
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4856569170951843,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0085906717300415,
                "rejected_mean_error": 2.4380121835708617,
                "gap_rejected_minus_accepted": 1.4294215118408202
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0842162072658539,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7545593354267816,
                "rejected_mean_error": 2.0469047092577184,
                "gap_rejected_minus_accepted": 1.292345373830937
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8665474891662597,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4903555199835035,
                "rejected_mean_error": 3.866802663803101,
                "gap_rejected_minus_accepted": 2.3764471438195973
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.4671385884284973,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2555268394118324,
                "rejected_mean_error": 3.1304212638310025,
                "gap_rejected_minus_accepted": 1.87489442441917
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4781834483146667,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.002833948612213,
                "rejected_mean_error": 2.4531665201187134,
                "gap_rejected_minus_accepted": 1.4503325715065003
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0610764920711517,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7496914778436933,
                "rejected_mean_error": 2.057590884958359,
                "gap_rejected_minus_accepted": 1.3078994071146655
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9898426691452139,
            "spearman": 0.9871279482088396,
            "auroc_top30_bad": 0.993731778425656,
            "mae": 0.07160714374001535,
            "mse": 0.011431293816543406,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9928571428571429,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7032143348837142,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0681043524827276
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19827467313834599
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5555746123194695
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.90986031688395
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9847888832492928,
            "spearman": 0.9848432343739476,
            "auroc_top30_worst": 0.9868124392614188,
            "pairwise_seed_ranking": 0.9271428571428572,
            "predicted_best_mean_error": 1.6157983941691263,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08190408689635142,
            "gap_to_oracle": 0.0013178927557808695,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.024064907005855
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2324792037691388
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4047377164023263
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5215313829694475
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1248594760894775,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5881748789832706,
                "rejected_mean_error": 2.4257791485105242,
                "gap_rejected_minus_accepted": 0.8376042695272536
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8968679904937744,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5215313829694475,
                "rejected_mean_error": 2.123147074835641,
                "gap_rejected_minus_accepted": 0.6016156918661937
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7108526825904846,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4047377164023263,
                "rejected_mean_error": 1.9391328954696656,
                "gap_rejected_minus_accepted": 0.5343951790673394
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4471169412136078,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.2324792037691388,
                "rejected_mean_error": 1.8184206733249482,
                "gap_rejected_minus_accepted": 0.5859414695558094
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1112025260925296,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.6075470069098095,
                "rejected_mean_error": 2.5091017484664917,
                "gap_rejected_minus_accepted": 0.9015547415566822
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9239253997802734,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5441233646301997,
                "rejected_mean_error": 2.1584398303713117,
                "gap_rejected_minus_accepted": 0.614316465741112
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7267807126045227,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4260018536022732,
                "rejected_mean_error": 1.969403108528682,
                "gap_rejected_minus_accepted": 0.5434012549264089
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4740550518035889,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.242613216808864,
                "rejected_mean_error": 1.849398902484349,
                "gap_rejected_minus_accepted": 0.606785685675485
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
      "best_epoch": 154,
      "best_calib_loss": 0.009957846254110336,
      "train_time_sec": 57.33881950378418,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9999091388497608,
            "spearman": 0.9993304487035026,
            "auroc_top30_bad": 0.999979761904762,
            "mae": 0.009222539733094164,
            "mse": 0.00016158742971473,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6675809162276689,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.001100616455078125
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16850822983831168
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46726587915346024
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7863390445863208
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998895522115412,
            "spearman": 0.9998830431473162,
            "auroc_top30_worst": 0.9999603809523809,
            "pairwise_seed_ranking": 0.9715,
            "predicted_best_mean_error": 1.4522099460065365,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07610105758905417,
            "gap_to_oracle": 0.00024482417106641563,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5869057555198669
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7976444302558899
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0475808932781219
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.261426912466685
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.28643171787262,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3960826857089996,
                "rejected_mean_error": 2.5833663940429688,
                "gap_rejected_minus_accepted": 1.1872837083339691
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9073325097560883,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.261426912466685,
                "rejected_mean_error": 2.274963488769531,
                "gap_rejected_minus_accepted": 1.013536576302846
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.519912302494049,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0475808932781219,
                "rejected_mean_error": 1.9820412198066713,
                "gap_rejected_minus_accepted": 0.9344603265285494
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1099347472190857,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7976444302558899,
                "rejected_mean_error": 1.7538665986378987,
                "gap_rejected_minus_accepted": 0.9562221683820088
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3194589853286742,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4064897636903657,
                "rejected_mean_error": 2.6247021627426146,
                "gap_rejected_minus_accepted": 1.2182123990522489
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.931119292974472,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2696340291102728,
                "rejected_mean_error": 2.3043419270515444,
                "gap_rejected_minus_accepted": 1.0347078979412716
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5356705784797668,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0525262005925178,
                "rejected_mean_error": 2.0040958065986634,
                "gap_rejected_minus_accepted": 0.9515696060061456
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1174733638763428,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7986638699769973,
                "rejected_mean_error": 1.7715267148017884,
                "gap_rejected_minus_accepted": 0.972862844824791
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9877885810167408,
            "spearman": 0.9858487848881948,
            "auroc_top30_bad": 0.9950361904761905,
            "mae": 0.10473441061545163,
            "mse": 0.021654561724881886,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.778843552915924,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07011808598041534
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18188142881393432
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5132309550404549
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9134459078550339
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9760212362540149,
            "spearman": 0.9794806673156273,
            "auroc_top30_worst": 0.9713371428571429,
            "pairwise_seed_ranking": 0.9244,
            "predicted_best_mean_error": 1.8265802915096283,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.09103913402557362,
            "gap_to_oracle": 0.0014073891639709846,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7650844955444336
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0409779735864737
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3406237953186035
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6187404522509463
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.586005020141602,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7660966460969714,
                "rejected_mean_error": 3.119376022338867,
                "gap_rejected_minus_accepted": 1.3532793762418958
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.3261359333992004,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.6176912526310827,
                "rejected_mean_error": 2.7508115844604686,
                "gap_rejected_minus_accepted": 1.1331203318293859
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9552255868911743,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3406237953186035,
                "rejected_mean_error": 2.462225372123718,
                "gap_rejected_minus_accepted": 1.1216015768051146
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3776643574237823,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0424985314329591,
                "rejected_mean_error": 2.1883443856061207,
                "gap_rejected_minus_accepted": 1.1458458541731615
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.631311273574829,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7773297497961256,
                "rejected_mean_error": 3.1802265071868896,
                "gap_rejected_minus_accepted": 1.402896757390764
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.350669264793396,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6289409185475845,
                "rejected_mean_error": 2.774490549450829,
                "gap_rejected_minus_accepted": 1.1455496309032445
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.976771891117096,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.345281798839569,
                "rejected_mean_error": 2.4899570522308347,
                "gap_rejected_minus_accepted": 1.1446752533912656
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3639661073684692,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0468678124367246,
                "rejected_mean_error": 2.2109742470603577,
                "gap_rejected_minus_accepted": 1.1641064346236332
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9641166734279047,
            "spearman": 0.972977686796959,
            "auroc_top30_bad": 0.998728380952381,
            "mae": 0.15906304286671802,
            "mse": 0.08379912579770525,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 0.996,
            "same_context_pred_std": 0.6608551732992263,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10899960500001907
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20908564896583556
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.46643749344348906
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7791996428012848
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9612116021420181,
            "spearman": 0.9892996088957499,
            "auroc_top30_worst": 0.9976076190476191,
            "pairwise_seed_ranking": 0.9304,
            "predicted_best_mean_error": 1.6528549263477326,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07514530801773067,
            "gap_to_oracle": 0.0013262237310409652,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.517112813949585
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7496541883700933
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.009808546257019
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2601140747700672
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5993130683898924,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5073748497433133,
                "rejected_mean_error": 3.6666406288146973,
                "gap_rejected_minus_accepted": 2.159265779071384
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.146293342113495,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.259395702289797,
                "rejected_mean_error": 3.112054349896245,
                "gap_rejected_minus_accepted": 1.852658647606448
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4901725053787231,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.009808546257019,
                "rejected_mean_error": 2.436794309043884,
                "gap_rejected_minus_accepted": 1.4269857627868652
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.116745114326477,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7505437169973843,
                "rejected_mean_error": 2.04824610580884,
                "gap_rejected_minus_accepted": 1.2977023888114558
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5735107421875,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5123685675197178,
                "rejected_mean_error": 3.668685235977173,
                "gap_rejected_minus_accepted": 2.156316668457455
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.161667823791504,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2576088302913198,
                "rejected_mean_error": 3.124241386141096,
                "gap_rejected_minus_accepted": 1.8666325558497763
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4677192568778992,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0028930821418762,
                "rejected_mean_error": 2.4531073865890503,
                "gap_rejected_minus_accepted": 1.450214304447174
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.116442084312439,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7483033518942576,
                "rejected_mean_error": 2.058058542363784,
                "gap_rejected_minus_accepted": 1.3097551904695264
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.984488140881882,
            "spearman": 0.9731587013164572,
            "auroc_top30_bad": 0.9721039844509233,
            "mae": 0.10223603060701862,
            "mse": 0.02248079848478923,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.716511477512565,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06208508695874895
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18841926800353187
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5564913846339499
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9160994667950131
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.9501708513393284,
            "spearman": 0.9176411730286329,
            "auroc_top30_worst": 0.9325947521865889,
            "pairwise_seed_ranking": 0.9271428571428572,
            "predicted_best_mean_error": 1.616142260176795,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08156022088868276,
            "gap_to_oracle": 0.001661758763449539,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0276642986706326
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.235586062840053
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4211531632287162
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5288763361885434
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.252317476272583,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5908574931205266,
                "rejected_mean_error": 2.401635621275221,
                "gap_rejected_minus_accepted": 0.8107781281546942
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9890709519386292,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5288763361885434,
                "rejected_mean_error": 2.1011122151783534,
                "gap_rejected_minus_accepted": 0.5722358789898101
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7047566771507263,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4211531632287162,
                "rejected_mean_error": 1.9227174486432757,
                "gap_rejected_minus_accepted": 0.5015642854145594
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4940155744552612,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.235586062840053,
                "rejected_mean_error": 1.8173850536346436,
                "gap_rejected_minus_accepted": 0.5817989907945906
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3296892881393436,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.609111726284027,
                "rejected_mean_error": 2.4950192740985324,
                "gap_rejected_minus_accepted": 0.8859075478145053
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0213347673416138,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5509638695489794,
                "rejected_mean_error": 2.137918315614973,
                "gap_rejected_minus_accepted": 0.5869544460659935
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.716535210609436,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4393715143203736,
                "rejected_mean_error": 1.9560334478105819,
                "gap_rejected_minus_accepted": 0.5166619334902083
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.5146245658397675,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.2477925675255912,
                "rejected_mean_error": 1.8476724522454397,
                "gap_rejected_minus_accepted": 0.5998798847198485
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
      "best_epoch": 145,
      "best_calib_loss": 0.009089376777410507,
      "train_time_sec": 56.408663272857666,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9998605812158348,
            "spearman": 0.9992031359799884,
            "auroc_top30_bad": 0.9999805714285713,
            "mae": 0.00875024268203415,
            "mse": 0.0001601841840773696,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6661540400270076,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0015784522593021394
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.16852358113378285
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.467267242693156
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7863520828559994
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1139734886761754
              }
            ]
          },
          "simvla_only": {
            "n": 5000,
            "contexts": 1000,
            "pearson": 0.9998189269541944,
            "spearman": 0.9998540228021504,
            "auroc_top30_worst": 0.9999270476190476,
            "pairwise_seed_ranking": 0.9659,
            "predicted_best_mean_error": 1.4523267944157123,
            "seed0_mean_error": 1.5283110035955907,
            "random_seed_mean_error": 1.5151066114902496,
            "oracle_best_mean_error": 1.45196512183547,
            "improvement_over_seed0": 0.07598420917987836,
            "gap_to_oracle": 0.0003616725802422227,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5869190384149552
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7975940257072449
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0475890837669373
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2614361078898113
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5148110565423965
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2826958894729614,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.3960932523674434,
                "rejected_mean_error": 2.5832712941169738,
                "gap_rejected_minus_accepted": 1.1871780417495303
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9018567204475403,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2614361078898113,
                "rejected_mean_error": 2.2749359025001525,
                "gap_rejected_minus_accepted": 1.0134997946103412
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5083807706832886,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0475890837669373,
                "rejected_mean_error": 1.9820330293178559,
                "gap_rejected_minus_accepted": 0.9344439455509186
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0980284810066223,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.7975940257072449,
                "rejected_mean_error": 1.7538834001541137,
                "gap_rejected_minus_accepted": 0.9562893744468688
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3297866582870483,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.40648382494847,
                "rejected_mean_error": 2.624755611419678,
                "gap_rejected_minus_accepted": 1.218271786471208
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9299704134464264,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2696382451454797,
                "rejected_mean_error": 2.304329278945923,
                "gap_rejected_minus_accepted": 1.0346910338004431
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5194490551948547,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0525217214226723,
                "rejected_mean_error": 2.004100285768509,
                "gap_rejected_minus_accepted": 0.9515785643458368
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1029203236103058,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7986315823793412,
                "rejected_mean_error": 1.7715374773343404,
                "gap_rejected_minus_accepted": 0.9729058949549992
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.988686689558723,
            "spearman": 0.9861376205867898,
            "auroc_top30_bad": 0.9956358095238095,
            "mae": 0.10023983921678736,
            "mse": 0.0199994594659597,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7773303381106169,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07352686578035354
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.18292443900108338
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5121786598324776
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9127992016553879
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.3029261555254459
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9807443723139172,
            "spearman": 0.9855545558749158,
            "auroc_top30_worst": 0.9846704761904762,
            "pairwise_seed_ranking": 0.9396,
            "predicted_best_mean_error": 1.8260491995811463,
            "seed0_mean_error": 1.917619425535202,
            "random_seed_mean_error": 1.8991771894693374,
            "oracle_best_mean_error": 1.8251729023456573,
            "improvement_over_seed0": 0.09157022595405562,
            "gap_to_oracle": 0.0008762972354889875,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7719974727630615
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0400900130088513
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3399151166915892
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.6115965712299225
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.901424583721161
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6335621118545536,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7656090909110176,
                "rejected_mean_error": 3.123764019012451,
                "gap_rejected_minus_accepted": 1.3581549281014336
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.336353063583374,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.610605256534564,
                "rejected_mean_error": 2.772024294819695,
                "gap_rejected_minus_accepted": 1.1614190382851308
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.959339201450348,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3399151166915892,
                "rejected_mean_error": 2.4629340507507322,
                "gap_rejected_minus_accepted": 1.123018934059143
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4230636954307556,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.041082766871102,
                "rejected_mean_error": 2.1888173144298784,
                "gap_rejected_minus_accepted": 1.1477345475587764
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6425129175186157,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7775671797328525,
                "rejected_mean_error": 3.1780896377563477,
                "gap_rejected_minus_accepted": 1.4005224580234952
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.371105372905731,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.6223896655806884,
                "rejected_mean_error": 2.793936332066854,
                "gap_rejected_minus_accepted": 1.1715466664861656
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.9744131565093994,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3440924496650697,
                "rejected_mean_error": 2.4911464014053344,
                "gap_rejected_minus_accepted": 1.1470539517402647
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4315780103206635,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0463544064097934,
                "rejected_mean_error": 2.2111472127271847,
                "gap_rejected_minus_accepted": 1.1647928063173913
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9652173254706864,
            "spearman": 0.9669299148522968,
            "auroc_top30_bad": 0.9979558095238096,
            "mae": 0.15231959153385832,
            "mse": 0.07972890476785463,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6517341771767412,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09124870240688324
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20605652627944945
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.48675336372852324
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.7787353755156199
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.2224939480662347
              }
            ]
          },
          "simvla_only": {
            "n": 1250,
            "contexts": 250,
            "pearson": 0.9720680329519982,
            "spearman": 0.9921321544525789,
            "auroc_top30_worst": 0.9986925714285715,
            "pairwise_seed_ranking": 0.918,
            "predicted_best_mean_error": 1.654219036579132,
            "seed0_mean_error": 1.7280002343654632,
            "random_seed_mean_error": 1.7201814349889755,
            "oracle_best_mean_error": 1.6515287026166916,
            "improvement_over_seed0": 0.07378119778633119,
            "gap_to_oracle": 0.00269033396244045,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5032183794975281
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7507954518764447
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0103407253265382
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2592576899762347
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.7233014276504517
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.689309930801392,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4924558461507162,
                "rejected_mean_error": 3.800911661148071,
                "gap_rejected_minus_accepted": 2.308455814997355
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1809002161026,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.2581361925334789,
                "rejected_mean_error": 3.1158248311795367,
                "gap_rejected_minus_accepted": 1.8576886386460578
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4731987118721008,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.0103407253265382,
                "rejected_mean_error": 2.436262129974365,
                "gap_rejected_minus_accepted": 1.425921404647827
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0856282711029053,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.7518295384824466,
                "rejected_mean_error": 2.047816583797288,
                "gap_rejected_minus_accepted": 1.2959870453148414
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6901524782180783,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4936056844393413,
                "rejected_mean_error": 3.8375511837005614,
                "gap_rejected_minus_accepted": 2.34394549926122
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2103903889656067,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2559014485481588,
                "rejected_mean_error": 3.129309328775557,
                "gap_rejected_minus_accepted": 1.8734078802273983
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4555878043174744,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.0049522252082825,
                "rejected_mean_error": 2.451048243522644,
                "gap_rejected_minus_accepted": 1.4460960183143614
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.07021564245224,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.7483033518942576,
                "rejected_mean_error": 2.058058542363784,
                "gap_rejected_minus_accepted": 1.3097551904695264
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 1400,
            "pearson": 0.9848558549441736,
            "spearman": 0.9726442673970458,
            "auroc_top30_bad": 0.9706729834791059,
            "mae": 0.09501368910606418,
            "mse": 0.019371282162895034,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.9785714285714285,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7079440328587155,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.055689718361411775
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1883617062653814
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5557268450515611
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9164492595479602
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.1861764596828392
              }
            ]
          },
          "simvla_only": {
            "n": 700,
            "contexts": 140,
            "pearson": 0.95223302596277,
            "spearman": 0.9139594745528633,
            "auroc_top30_worst": 0.9289504373177842,
            "pairwise_seed_ranking": 0.9278571428571428,
            "predicted_best_mean_error": 1.6161297040326255,
            "seed0_mean_error": 1.6977024810654777,
            "random_seed_mean_error": 1.668839773961476,
            "oracle_best_mean_error": 1.6144805014133454,
            "improvement_over_seed0": 0.08157277703285226,
            "gap_to_oracle": 0.0016492026192800324,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.0265776685306005
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.2346799509865898
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.4235336555753435
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5309849836712792
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.6719353059359958
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.165917921066284,
                "accepted_n": 630,
                "rejected_n": 70,
                "accepted_mean_error": 1.5903044588982114,
                "rejected_mean_error": 2.406612929276058,
                "gap_rejected_minus_accepted": 0.8163084703778465
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9450015127658844,
                "accepted_n": 525,
                "rejected_n": 175,
                "accepted_mean_error": 1.5309849836712792,
                "rejected_mean_error": 2.094786272730146,
                "gap_rejected_minus_accepted": 0.5638012890588668
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7462603449821472,
                "accepted_n": 350,
                "rejected_n": 350,
                "accepted_mean_error": 1.4235336555753435,
                "rejected_mean_error": 1.9203369562966484,
                "gap_rejected_minus_accepted": 0.49680330072130485
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4724744856357574,
                "accepted_n": 175,
                "rejected_n": 525,
                "accepted_mean_error": 1.2346799509865898,
                "rejected_mean_error": 1.8176870909191314,
                "gap_rejected_minus_accepted": 0.5830071399325416
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.2098257780075072,
                "accepted_n": 126,
                "rejected_n": 14,
                "accepted_mean_error": 1.609111726284027,
                "rejected_mean_error": 2.4950192740985324,
                "gap_rejected_minus_accepted": 0.8859075478145053
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9657988250255585,
                "accepted_n": 105,
                "rejected_n": 35,
                "accepted_mean_error": 1.5523668311891101,
                "rejected_mean_error": 2.13370943069458,
                "gap_rejected_minus_accepted": 0.58134259950547
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.757485806941986,
                "accepted_n": 70,
                "rejected_n": 70,
                "accepted_mean_error": 1.4411442739622933,
                "rejected_mean_error": 1.954260688168662,
                "gap_rejected_minus_accepted": 0.5131164142063687
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4899241924285889,
                "accepted_n": 35,
                "rejected_n": 105,
                "accepted_mean_error": 1.246722057887486,
                "rejected_mean_error": 1.8480292887914749,
                "gap_rejected_minus_accepted": 0.6013072309039889
              }
            ]
          }
        }
      }
    }
  ]
}
```
