# Stage 6 Experiments: holdout_object_bowl

```json
{
  "split": "holdout_object_bowl",
  "results": [
    {
      "variant": "action_only_baseline",
      "feature_mode": "A0_action_flat",
      "model_kind": "mlp",
      "train_setting": "mixed",
      "train_rows": 10000,
      "input_dim": 70,
      "best_epoch": 103,
      "best_calib_loss": 0.08970356732606888,
      "train_time_sec": 16.839507818222046,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.8776130906233394,
            "spearman": 0.8291401465252911,
            "auroc_top30_bad": 0.9058543095238096,
            "mae": 0.19289382995963097,
            "mse": 0.19690883812058488,
            "expert_lt_perturb_large": 0.984,
            "expert_lt_other_task": 0.554,
            "expert_lt_simvla_seed0": 0.977,
            "same_context_pred_std": 0.7147128199468457,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.4548993082344532
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.4885540401220322
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6728718383580446
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9535442976335684
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
            "pearson": 0.9982195423204053,
            "spearman": 0.9967869575594012,
            "auroc_top30_worst": 0.9991929523809524,
            "pairwise_seed_ranking": 0.8701,
            "predicted_best_mean_error": 1.5363175510764122,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.07929077693820008,
            "gap_to_oracle": 0.007458316892385408,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6707805642485618
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8091836241006851
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.010945223081112
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2418507623275121
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.778451037406922,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4058191540175013,
                "rejected_mean_error": 3.4554154858589174,
                "gap_rejected_minus_accepted": 2.049596331841416
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9720708727836609,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2418507623275121,
                "rejected_mean_error": 2.7175628618240357,
                "gap_rejected_minus_accepted": 1.4757120994965236
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3926147818565369,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.010945223081112,
                "rejected_mean_error": 2.2106123513221743,
                "gap_rejected_minus_accepted": 1.1996671282410623
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0054554045200348,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8091836241006851,
                "rejected_mean_error": 1.8779771749019623,
                "gap_rejected_minus_accepted": 1.0687935508012771
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7953820943832404,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106771012478405,
                "rejected_mean_error": 3.459989368915558,
                "gap_rejected_minus_accepted": 2.0493122676677173
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9908082783222198,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2434188873370489,
                "rejected_mean_error": 2.732176650047302,
                "gap_rejected_minus_accepted": 1.4887577627102533
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4084338545799255,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0043328621983527,
                "rejected_mean_error": 2.2268837938308716,
                "gap_rejected_minus_accepted": 1.222550931632519
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0096206068992615,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7998697680234909,
                "rejected_mean_error": 1.887521181344986,
                "gap_rejected_minus_accepted": 1.087651413321495
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.5575880196000188,
            "spearman": 0.5243788177508452,
            "auroc_top30_bad": 0.6845862857142858,
            "mae": 0.4598849759578705,
            "mse": 0.5001665718179233,
            "expert_lt_perturb_large": 0.98,
            "expert_lt_other_task": 0.496,
            "expert_lt_simvla_seed0": 0.968,
            "same_context_pred_std": 0.6200668795517139,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.518568251311779
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.7676790344715119
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.9437627476334571
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.1460426507870356
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
            "pearson": 0.480706980890634,
            "spearman": 0.5040957420132749,
            "auroc_top30_worst": 0.740263619047619,
            "pairwise_seed_ranking": 0.7496,
            "predicted_best_mean_error": 1.4830085163116455,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.04578530740737907,
            "gap_to_oracle": 0.020165494203567613,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9634155406951904
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1938177324258363
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.358143521785736
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4531987857208577
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0566066741943363,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5126370952924093,
                "rejected_mean_error": 1.7512497591972351,
                "gap_rejected_minus_accepted": 0.23861266390482583
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.7107970118522644,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4529753317827858,
                "rejected_mean_error": 1.7865337579014202,
                "gap_rejected_minus_accepted": 0.3335584261186344
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4744112491607666,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.358143521785736,
                "rejected_mean_error": 1.7148532015800475,
                "gap_rejected_minus_accepted": 0.35670967979431145
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2130836248397827,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.195593933327891,
                "rejected_mean_error": 1.650375721421542,
                "gap_rejected_minus_accepted": 0.4547817880936509
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0663034915924072,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5036956691741943,
                "rejected_mean_error": 1.7546772146224976,
                "gap_rejected_minus_accepted": 0.2509815454483033
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.6945205926895142,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4371952857563202,
                "rejected_mean_error": 1.8006815475130837,
                "gap_rejected_minus_accepted": 0.3634862617567636
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4853681921958923,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.3555711975097657,
                "rejected_mean_error": 1.7020164499282837,
                "gap_rejected_minus_accepted": 0.346445252418518
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2318654656410217,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1667507205690657,
                "rejected_mean_error": 1.6507655643524333,
                "gap_rejected_minus_accepted": 0.48401484378336757
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.48392965988706643,
            "spearman": 0.4344273204906387,
            "auroc_top30_bad": 0.600152,
            "mae": 0.6250551493525505,
            "mse": 0.7651101331543134,
            "expert_lt_perturb_large": 0.932,
            "expert_lt_other_task": 0.492,
            "expert_lt_simvla_seed0": 0.912,
            "same_context_pred_std": 0.6382117645469394,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.49036196094751355
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.549902933549881
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1267112057089805
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3102863956451416
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
            "pearson": 0.18233859192689206,
            "spearman": 0.0647349979743987,
            "auroc_top30_worst": 0.3964678095238095,
            "pairwise_seed_ranking": 0.7088,
            "predicted_best_mean_error": 1.7622223135232926,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.0449262678623199,
            "gap_to_oracle": 0.03833551335334784,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 1.502430584192276
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.870466172026518
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.8329879264354705
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.7931745026919887
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6293432474136353,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.7441258503595989,
                "rejected_mean_error": 2.327463221549988,
                "gap_rejected_minus_accepted": 0.5833373711903891
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8578110933303833,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.7937816660075967,
                "rejected_mean_error": 1.8284379019143102,
                "gap_rejected_minus_accepted": 0.03465623590671352
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3220092058181763,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.8329879264354705,
                "rejected_mean_error": 1.7719312485218048,
                "gap_rejected_minus_accepted": -0.06105667791366565
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.081472247838974,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.8690762772156408,
                "rejected_mean_error": 1.7802066270862342,
                "gap_rejected_minus_accepted": -0.08886965012940662
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.6478846311569213,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.7481526039706337,
                "rejected_mean_error": 2.3381123781204223,
                "gap_rejected_minus_accepted": 0.5899597741497886
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8812040388584137,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.7906932019613644,
                "rejected_mean_error": 1.8559923266607619,
                "gap_rejected_minus_accepted": 0.06529912469939747
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3035890460014343,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.8115771758556365,
                "rejected_mean_error": 1.8027199869155883,
                "gap_rejected_minus_accepted": -0.008857188940048166
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0747451186180115,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.8955817075948866,
                "rejected_mean_error": 1.7773556030370334,
                "gap_rejected_minus_accepted": -0.1182261045578532
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.6349871401384601,
            "spearman": 0.6061278354842659,
            "auroc_top30_bad": 0.7986380952380951,
            "mae": 0.46910624625086783,
            "mse": 0.47597264328267147,
            "expert_lt_perturb_large": 0.96,
            "expert_lt_other_task": 0.536,
            "expert_lt_simvla_seed0": 0.952,
            "same_context_pred_std": 0.6921594593268495,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6481805680990219
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.6005241494178772
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.836309788453579
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0706192361990612
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
            "pearson": 0.6967857886765177,
            "spearman": 0.6175987066871723,
            "auroc_top30_worst": 0.8629881904761905,
            "pairwise_seed_ranking": 0.7512,
            "predicted_best_mean_error": 1.5667593653202057,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.052562912940979034,
            "gap_to_oracle": 0.015616105079650833,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.7325766294002533
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0952250830447063
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2841392942905425
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4081300867836613
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.444601893424988,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.5204352684815725,
                "rejected_mean_error": 2.546185929775238,
                "gap_rejected_minus_accepted": 1.0257506612936655
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.118211269378662,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4070987042075416,
                "rejected_mean_error": 2.2693655987898,
                "gap_rejected_minus_accepted": 0.8622668945822585
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.7140794396400452,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2841392942905425,
                "rejected_mean_error": 1.9618813749313355,
                "gap_rejected_minus_accepted": 0.677742080640793
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3530691862106323,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0934056652049287,
                "rejected_mean_error": 1.7999220331425092,
                "gap_rejected_minus_accepted": 0.7065163679375805
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.47984037399292,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.5180010549227396,
                "rejected_mean_error": 2.53121328830719,
                "gap_rejected_minus_accepted": 1.0132122333844502
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.144103765487671,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.400471109119966,
                "rejected_mean_error": 2.2689281295216275,
                "gap_rejected_minus_accepted": 0.8684570204016615
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.719577968120575,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2499276628494262,
                "rejected_mean_error": 1.9887168936729431,
                "gap_rejected_minus_accepted": 0.7387892308235169
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.371792882680893,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0500756795444186,
                "rejected_mean_error": 1.8111005441390258,
                "gap_rejected_minus_accepted": 0.7610248645946072
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
      "best_epoch": 118,
      "best_calib_loss": 0.022046823054552078,
      "train_time_sec": 20.99737572669983,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9992077070468347,
            "spearman": 0.9980523489055653,
            "auroc_top30_bad": 0.9994834761904762,
            "mae": 0.025695935101440408,
            "mse": 0.001334779792482644,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7378851605054405,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00890707467496395
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19790469145774842
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740618480682373
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9270895003636678
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
            "pearson": 0.999371829132659,
            "spearman": 0.9989156390605733,
            "auroc_top30_worst": 0.99968,
            "pairwise_seed_ranking": 0.9335,
            "predicted_best_mean_error": 1.5309088313281536,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08469949668645871,
            "gap_to_oracle": 0.00204959714412678,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6663484738469124
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8075453007459641
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0103994004130363
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2416321678082147
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7333501577377337,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.405695105996397,
                "rejected_mean_error": 3.4565319180488587,
                "gap_rejected_minus_accepted": 2.050836812052462
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9638394713401794,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2416321678082147,
                "rejected_mean_error": 2.7182186453819277,
                "gap_rejected_minus_accepted": 1.476586477573713
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.3974528312683105,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0103994004130363,
                "rejected_mean_error": 2.2111581739902495,
                "gap_rejected_minus_accepted": 1.2007587735772132
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0130921304225922,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8075453007459641,
                "rejected_mean_error": 1.8785232826868694,
                "gap_rejected_minus_accepted": 1.0709779819409053
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7678832054138187,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4107309549715783,
                "rejected_mean_error": 3.4595046854019165,
                "gap_rejected_minus_accepted": 2.048773730430338
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9835896790027618,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2435279713074365,
                "rejected_mean_error": 2.7318493981361387,
                "gap_rejected_minus_accepted": 1.4883214268287022
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.40712571144104,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0039747820496558,
                "rejected_mean_error": 2.2272418739795685,
                "gap_rejected_minus_accepted": 1.2232670919299127
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0131801664829254,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7995908538103104,
                "rejected_mean_error": 1.8876141527493795,
                "gap_rejected_minus_accepted": 1.0880232989390692
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9582954286089833,
            "spearman": 0.9454893613367097,
            "auroc_top30_bad": 0.9501577142857144,
            "mae": 0.17275789070818573,
            "mse": 0.05368616026746611,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.98,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6083800146413053,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.10309189838171005
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24656951711177827
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.702959070289135
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0493362060149511
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
            "pearson": 0.8947553240383744,
            "spearman": 0.8882326058448677,
            "auroc_top30_worst": 0.9322300952380953,
            "pairwise_seed_ranking": 0.8368,
            "predicted_best_mean_error": 1.4744187185764313,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.05437510514259336,
            "gap_to_oracle": 0.011575696468353325,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9427393231391906
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.0373468595819595
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2096281081199647
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3718864882170265
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.029641318321228,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4608238104714288,
                "rejected_mean_error": 2.2175693225860598,
                "gap_rejected_minus_accepted": 0.7567455121146309
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8298372626304626,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3712239467728735,
                "rejected_mean_error": 2.031265539864001,
                "gap_rejected_minus_accepted": 0.6600415930911274
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5511868000030518,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2096281081199647,
                "rejected_mean_error": 1.863368615245819,
                "gap_rejected_minus_accepted": 0.6537405071258544
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.243753969669342,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.0384191386996748,
                "rejected_mean_error": 1.7028791480155994,
                "gap_rejected_minus_accepted": 0.6644600093159245
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0474919080734253,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4541180149714152,
                "rejected_mean_error": 2.2008761024475096,
                "gap_rejected_minus_accepted": 0.7467580874760944
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8414433002471924,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3587029471116907,
                "rejected_mean_error": 2.0336667431725397,
                "gap_rejected_minus_accepted": 0.674963796060849
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5433842539787292,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.197012873649597,
                "rejected_mean_error": 1.8605747737884522,
                "gap_rejected_minus_accepted": 0.6635619001388551
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2108678221702576,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.0161031389993334,
                "rejected_mean_error": 1.7015184929026639,
                "gap_rejected_minus_accepted": 0.6854153539033305
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9603868638219438,
            "spearman": 0.9569249298522732,
            "auroc_top30_bad": 0.9691961904761905,
            "mae": 0.2043533582817763,
            "mse": 0.07841924652846533,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.670892907693589,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.12100390046834945
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2402049795627594
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7132724471926689
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.059611133948962
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
            "pearson": 0.96144636016489,
            "spearman": 0.9445337572696048,
            "auroc_top30_worst": 0.9913386666666666,
            "pairwise_seed_ranking": 0.868,
            "predicted_best_mean_error": 1.7297961024045945,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.07735247898101805,
            "gap_to_oracle": 0.005909302234649694,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9848449087142944
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1458179442546306
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2977898164749146
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4557161591708787
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.564095950126648,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6565652590857611,
                "rejected_mean_error": 3.1155085430145264,
                "gap_rejected_minus_accepted": 1.4589432839287653
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2008877992630005,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4550738888082027,
                "rejected_mean_error": 2.842396966565531,
                "gap_rejected_minus_accepted": 1.3873230777573284
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.652834713459015,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2977898164749146,
                "rejected_mean_error": 2.307129358482361,
                "gap_rejected_minus_accepted": 1.0093395420074462
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4510613679885864,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1462969890417762,
                "rejected_mean_error": 2.021647307127237,
                "gap_rejected_minus_accepted": 0.8753503180854609
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5670088291168214,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6581069881386228,
                "rejected_mean_error": 3.1485229206085203,
                "gap_rejected_minus_accepted": 1.4904159324698976
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.2126073837280273,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4545739422188724,
                "rejected_mean_error": 2.8536796531979998,
                "gap_rejected_minus_accepted": 1.3991057109791274
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6315260529518127,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.299152046918869,
                "rejected_mean_error": 2.315145115852356,
                "gap_rejected_minus_accepted": 1.0159930689334868
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.4535982012748718,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1452285595356473,
                "rejected_mean_error": 2.0301483748430873,
                "gap_rejected_minus_accepted": 0.88491981530744
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9632558972252524,
            "spearman": 0.9588340366164233,
            "auroc_top30_bad": 0.9728464761904762,
            "mae": 0.17632112887473778,
            "mse": 0.058039933519081106,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.984,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6326951132177675,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.1136711809039116
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2477662058830261
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6044011020183563
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9498068838119507
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
            "pearson": 0.9671321492863163,
            "spearman": 0.9448938634840727,
            "auroc_top30_worst": 0.9875291428571429,
            "pairwise_seed_ranking": 0.8708,
            "predicted_best_mean_error": 1.5603809152841568,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.0589413629770279,
            "gap_to_oracle": 0.009237655043601967,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5807627713680268
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.907610781204242
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1324242176532746
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3156044564839364
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.722475171089173,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.475945510678821,
                "rejected_mean_error": 2.94659375,
                "gap_rejected_minus_accepted": 1.4706482393211788
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1700626015663147,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3145860132374656,
                "rejected_mean_error": 2.546312536294468,
                "gap_rejected_minus_accepted": 1.2317265230570023
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5939099788665771,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1324242176532746,
                "rejected_mean_error": 2.1135964515686037,
                "gap_rejected_minus_accepted": 0.981172233915329
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3037227988243103,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.909031664506315,
                "rejected_mean_error": 1.8615112137387377,
                "gap_rejected_minus_accepted": 0.9524795492324227
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.679202032089233,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4693299571673075,
                "rejected_mean_error": 2.969253168106079,
                "gap_rejected_minus_accepted": 1.4999232109387715
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.1404370069503784,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3006085192455965,
                "rejected_mean_error": 2.5653456581963434,
                "gap_rejected_minus_accepted": 1.264737138950747
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.54624742269516,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1259789867401122,
                "rejected_mean_error": 2.112665569782257,
                "gap_rejected_minus_accepted": 0.986686583042145
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.303134709596634,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8883589033096556,
                "rejected_mean_error": 1.8655826666138389,
                "gap_rejected_minus_accepted": 0.9772237633041833
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
      "best_epoch": 88,
      "best_calib_loss": 0.005437436979264021,
      "train_time_sec": 52.34044647216797,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9996721303013707,
            "spearman": 0.998729926280477,
            "auroc_top30_bad": 0.9997824761904762,
            "mae": 0.016798454066785054,
            "mse": 0.0005417601393050581,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.740110558326463,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.001281598210334778
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.197730584859848
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740298883199692
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9268116494655609
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
            "pearson": 0.9995417797710786,
            "spearman": 0.9992122587444714,
            "auroc_top30_worst": 0.9998739047619047,
            "pairwise_seed_ranking": 0.9549,
            "predicted_best_mean_error": 1.5304995752871036,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08510875272750873,
            "gap_to_oracle": 0.001640341103076759,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6664633402228355
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.807220923781395
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.010175767171383
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2414746992667516
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7581411123275763,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056647958424355,
                "rejected_mean_error": 3.4568047094345093,
                "gap_rejected_minus_accepted": 2.051139913592074
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9733923971652985,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2414746992667516,
                "rejected_mean_error": 2.718691051006317,
                "gap_rejected_minus_accepted": 1.4772163517395656
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4095916152000427,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.010175767171383,
                "rejected_mean_error": 2.211381807231903,
                "gap_rejected_minus_accepted": 1.20120604006052
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0285666584968567,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.807220923781395,
                "rejected_mean_error": 1.8786314083417257,
                "gap_rejected_minus_accepted": 1.0714104845603307
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7852761030197146,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106409323546623,
                "rejected_mean_error": 3.4603148889541626,
                "gap_rejected_minus_accepted": 2.0496739565995004
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9900500774383545,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.243178830186526,
                "rejected_mean_error": 2.732896821498871,
                "gap_rejected_minus_accepted": 1.4897179913123448
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4205546975135803,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0038357358574868,
                "rejected_mean_error": 2.2273809201717376,
                "gap_rejected_minus_accepted": 1.2235451843142509
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.023685783147812,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7986470767259598,
                "rejected_mean_error": 1.8879287451108298,
                "gap_rejected_minus_accepted": 1.0892816683848698
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9899894234809894,
            "spearman": 0.98750539555809,
            "auroc_top30_bad": 0.9907855238095238,
            "mae": 0.0735993216946721,
            "mse": 0.01183781687833019,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7002598256991461,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04156038624048233
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22564623301029205
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.679669776570797
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.032915438357989
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
            "pearson": 0.9822838759845669,
            "spearman": 0.9821204877571122,
            "auroc_top30_worst": 0.9914666666666666,
            "pairwise_seed_ranking": 0.8784,
            "predicted_best_mean_error": 1.4708061666488648,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.05798765707015985,
            "gap_to_oracle": 0.007963144540786837,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8776139998435974
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9785064455026236
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1687025218963623
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3569479331787206
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0747299909591677,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4577677637736002,
                "rejected_mean_error": 2.245073742866516,
                "gap_rejected_minus_accepted": 0.7873059790929158
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9150660336017609,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3563341663130575,
                "rejected_mean_error": 2.075839738876294,
                "gap_rejected_minus_accepted": 0.7195055725632367
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5156483054161072,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1687025218963623,
                "rejected_mean_error": 1.9042942014694213,
                "gap_rejected_minus_accepted": 0.735591679573059
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1471631824970245,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9789879866682303,
                "rejected_mean_error": 1.7227318167304788,
                "gap_rejected_minus_accepted": 0.7437438300622485
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0897156476974486,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4523541937934028,
                "rejected_mean_error": 2.216750493049622,
                "gap_rejected_minus_accepted": 0.764396299256219
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9068443775177002,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3493797842831534,
                "rejected_mean_error": 2.061340258235023,
                "gap_rejected_minus_accepted": 0.7119604739518697
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5161998271942139,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.157300905227661,
                "rejected_mean_error": 1.9002867422103882,
                "gap_rejected_minus_accepted": 0.7429858369827271
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.177469551563263,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9614670106342861,
                "rejected_mean_error": 1.7199253168973057,
                "gap_rejected_minus_accepted": 0.7584583062630196
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9770967629870034,
            "spearman": 0.9799821880277176,
            "auroc_top30_bad": 0.9856761904761905,
            "mae": 0.1400221747584641,
            "mse": 0.04466342095130704,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7207936062207195,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0789405727982521
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20455630996227264
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.695360105407238
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0506056761344273
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
            "pearson": 0.9567908240903225,
            "spearman": 0.9612287055543718,
            "auroc_top30_worst": 0.9815984761904761,
            "pairwise_seed_ranking": 0.9184,
            "predicted_best_mean_error": 1.7258346084356309,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08131397294998166,
            "gap_to_oracle": 0.0019478082656860796,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9485604496002197
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1117448802941885
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.3000023538589478
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.460786075480203
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.3657703399658208,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.649652348836263,
                "rejected_mean_error": 3.1777247352600098,
                "gap_rejected_minus_accepted": 1.5280723864237467
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.925415575504303,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.459809090309998,
                "rejected_mean_error": 2.8282216189387506,
                "gap_rejected_minus_accepted": 1.3684125286287525
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6378686428070068,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.3000023538589478,
                "rejected_mean_error": 2.3049168210983275,
                "gap_rejected_minus_accepted": 1.0049144672393797
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3624354004859924,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1126660089523266,
                "rejected_mean_error": 2.032881561949006,
                "gap_rejected_minus_accepted": 0.9202155529966796
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.362597608566284,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6526559489303165,
                "rejected_mean_error": 3.197582273483276,
                "gap_rejected_minus_accepted": 1.5449263245529596
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9399695694446564,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.457839541097376,
                "rejected_mean_error": 2.8439865263681563,
                "gap_rejected_minus_accepted": 1.3861469852707804
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6218408942222595,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2962441251277923,
                "rejected_mean_error": 2.3180530376434327,
                "gap_rejected_minus_accepted": 1.0218089125156404
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3570009171962738,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1117005892216214,
                "rejected_mean_error": 2.041443894253695,
                "gap_rejected_minus_accepted": 0.9297433050320738
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9912292154203594,
            "spearman": 0.9900941513967204,
            "auroc_top30_bad": 0.9959565714285714,
            "mae": 0.07923879721891135,
            "mse": 0.013650083118557496,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.988,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7377335823115914,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04796569609642029
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1970689197063446
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5902703624725342
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9331694859822591
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
            "pearson": 0.9839755633635676,
            "spearman": 0.9831414614665355,
            "auroc_top30_worst": 0.9961630476190476,
            "pairwise_seed_ranking": 0.9328,
            "predicted_best_mean_error": 1.553466037273407,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06585624098777765,
            "gap_to_oracle": 0.002322777032852219,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5695909769535065
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8710260896537548
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.118213173532486
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3109996911368644
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.633352875709534,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4774259408579933,
                "rejected_mean_error": 2.9332698783874513,
                "gap_rejected_minus_accepted": 1.455843937529458
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.065606415271759,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3100910199808082,
                "rejected_mean_error": 2.5597687940628004,
                "gap_rejected_minus_accepted": 1.2496777740819922
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5575488805770874,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.118213173532486,
                "rejected_mean_error": 2.127807495689392,
                "gap_rejected_minus_accepted": 1.009594322156906
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2367822527885437,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8721869922103211,
                "rejected_mean_error": 1.8738189858077303,
                "gap_rejected_minus_accepted": 1.0016319935974092
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5965596675872797,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4691338721911114,
                "rejected_mean_error": 2.971017932891846,
                "gap_rejected_minus_accepted": 1.5018840607007344
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.060459554195404,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2979737759273957,
                "rejected_mean_error": 2.573166245505923,
                "gap_rejected_minus_accepted": 1.2751924695785275
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.571342945098877,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.105490219593048,
                "rejected_mean_error": 2.133154336929321,
                "gap_rejected_minus_accepted": 1.027664117336273
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.231493592262268,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.851890091858213,
                "rejected_mean_error": 1.8778689506857154,
                "gap_rejected_minus_accepted": 1.0259788588275023
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
      "best_epoch": 74,
      "best_calib_loss": 0.00937505904585123,
      "train_time_sec": 53.68815612792969,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999684461137839,
            "spearman": 0.9987732011016927,
            "auroc_top30_bad": 0.9998407142857142,
            "mae": 0.016012463313836805,
            "mse": 0.000543345333097119,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7408090642034668,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0010011550337076186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19769751229286195
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5739606753587723
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9267674689610799
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
            "pearson": 0.999659980576425,
            "spearman": 0.9994089629443159,
            "auroc_top30_worst": 0.999891619047619,
            "pairwise_seed_ranking": 0.9601,
            "predicted_best_mean_error": 1.530157472461462,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08545085555315035,
            "gap_to_oracle": 0.0012982382774351375,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6662908234000205
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8071469341516495
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0101518218874932
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2412827034552891
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7595301628112803,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4056848502357802,
                "rejected_mean_error": 3.456624219894409,
                "gap_rejected_minus_accepted": 2.0509393696586287
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9682148396968842,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2412827034552891,
                "rejected_mean_error": 2.7192670384407043,
                "gap_rejected_minus_accepted": 1.4779843349854151
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4182478785514832,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0101518218874932,
                "rejected_mean_error": 2.211405752515793,
                "gap_rejected_minus_accepted": 1.2012539306282997
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.028883159160614,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8071469341516495,
                "rejected_mean_error": 1.878656071551641,
                "gap_rejected_minus_accepted": 1.0715091373999914
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.783358597755432,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4106783449980949,
                "rejected_mean_error": 3.459978175163269,
                "gap_rejected_minus_accepted": 2.0492998301651744
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.985399216413498,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.243188991268476,
                "rejected_mean_error": 2.732866338253021,
                "gap_rejected_minus_accepted": 1.4896773469845452
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4245189428329468,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.003928101360798,
                "rejected_mean_error": 2.2272885546684265,
                "gap_rejected_minus_accepted": 1.2233604533076285
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0255863070487976,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7989475544691086,
                "rejected_mean_error": 1.8878285858631134,
                "gap_rejected_minus_accepted": 1.088881031394005
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9813608305088937,
            "spearman": 0.9815240514164377,
            "auroc_top30_bad": 0.9864411428571429,
            "mae": 0.09892567945524604,
            "mse": 0.021967015058642018,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6742551454334407,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07256305980682373
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23845071957111358
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6818709723830223
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0346579523324966
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
            "pearson": 0.9723552096434984,
            "spearman": 0.9726140425049874,
            "auroc_top30_worst": 0.9822110476190477,
            "pairwise_seed_ranking": 0.8808,
            "predicted_best_mean_error": 1.4683870794773102,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06040674424171444,
            "gap_to_oracle": 0.005544057369232247,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.886559015750885
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9831573084378854
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1733292058944702
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3621435629279375
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.026426315307617,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4560248970455594,
                "rejected_mean_error": 2.2607595434188843,
                "gap_rejected_minus_accepted": 0.8047346463733249
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8523630499839783,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3616261862639811,
                "rejected_mean_error": 2.0599974938474905,
                "gap_rejected_minus_accepted": 0.6983713075835094
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4792561531066895,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1733292058944702,
                "rejected_mean_error": 1.8996675174713136,
                "gap_rejected_minus_accepted": 0.7263383115768434
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1194840967655182,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9835838707872092,
                "rejected_mean_error": 1.721196585429262,
                "gap_rejected_minus_accepted": 0.7376127146420527
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0465354919433594,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4512835629781087,
                "rejected_mean_error": 2.226386170387268,
                "gap_rejected_minus_accepted": 0.7751026074091594
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8537276685237885,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3518130020661787,
                "rejected_mean_error": 2.0541178498949324,
                "gap_rejected_minus_accepted": 0.7023048478287537
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4793476462364197,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1620925693511963,
                "rejected_mean_error": 1.8954950780868531,
                "gap_rejected_minus_accepted": 0.7334025087356568
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.133307933807373,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9645285625306387,
                "rejected_mean_error": 1.718893884975005,
                "gap_rejected_minus_accepted": 0.7543653224443664
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9521090718168037,
            "spearman": 0.9646295064585952,
            "auroc_top30_bad": 0.9867017142857143,
            "mae": 0.18991614762059794,
            "mse": 0.1037063217354194,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.992,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6566871279782527,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09105226880311966
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22369087269306182
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6961776322245598
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0774960215806961
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
            "pearson": 0.9043063309371652,
            "spearman": 0.9536039843865501,
            "auroc_top30_worst": 0.9828693333333334,
            "pairwise_seed_ranking": 0.9276,
            "predicted_best_mean_error": 1.7260524109601973,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08109617042541517,
            "gap_to_oracle": 0.00216561079025257,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.944173113822937
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1251837794597332
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.288158084487915
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4948604050984007
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9924898743629456,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6658053927951388,
                "rejected_mean_error": 3.032347339630127,
                "gap_rejected_minus_accepted": 1.366541946834988
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.808592140674591,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.493583069794206,
                "rejected_mean_error": 2.727115488661745,
                "gap_rejected_minus_accepted": 1.2335324188675387
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5413623452186584,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.288158084487915,
                "rejected_mean_error": 2.3167610904693605,
                "gap_rejected_minus_accepted": 1.0286030059814455
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3088306784629822,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1255691843672682,
                "rejected_mean_error": 2.0285713229896927,
                "gap_rejected_minus_accepted": 0.9030021386224245
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9849097371101379,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6693937713570064,
                "rejected_mean_error": 3.0469418716430665,
                "gap_rejected_minus_accepted": 1.3775481002860601
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8187252879142761,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.497264362114636,
                "rejected_mean_error": 2.7269636449359713,
                "gap_rejected_minus_accepted": 1.2296992828213353
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5359838008880615,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.284268125295639,
                "rejected_mean_error": 2.330029037475586,
                "gap_rejected_minus_accepted": 1.045760912179947
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3173174560070038,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1344154576460521,
                "rejected_mean_error": 2.0337912915224696,
                "gap_rejected_minus_accepted": 0.8993758338764175
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9922548523066299,
            "spearman": 0.9903408354473286,
            "auroc_top30_bad": 0.997584,
            "mae": 0.07384527876274523,
            "mse": 0.01243207930140195,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7090571812394759,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05899597507715225
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20104231209754944
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5899284169197082
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9328523482640584
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
            "pearson": 0.9924332881170278,
            "spearman": 0.9862649809055879,
            "auroc_top30_worst": 0.9992899047619047,
            "pairwise_seed_ranking": 0.9044,
            "predicted_best_mean_error": 1.5542351884841918,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06508708977699285,
            "gap_to_oracle": 0.003091928243637021,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.569367743730545
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8781225097676119
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1159424583911897
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3089946638355885
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.501171898841858,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.475412024418513,
                "rejected_mean_error": 2.9513951263427733,
                "gap_rejected_minus_accepted": 1.4759831019242604
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9917482733726501,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.308265894969474,
                "rejected_mean_error": 2.5652325069561552,
                "gap_rejected_minus_accepted": 1.2569666119866811
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4598609805107117,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1159424583911897,
                "rejected_mean_error": 2.1300782108306886,
                "gap_rejected_minus_accepted": 1.014135752439499
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.210916817188263,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8793784651322106,
                "rejected_mean_error": 1.8714167115019122,
                "gap_rejected_minus_accepted": 0.9920382463697016
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.499494194984436,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4681327907244364,
                "rejected_mean_error": 2.980027666091919,
                "gap_rejected_minus_accepted": 1.5118948753674828
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9962184429168701,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2971497841059842,
                "rejected_mean_error": 2.5756120624996366,
                "gap_rejected_minus_accepted": 1.2784622783936523
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4766345024108887,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1031892199516296,
                "rejected_mean_error": 2.1354553365707396,
                "gap_rejected_minus_accepted": 1.03226611661911
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2121604979038239,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8636012578767444,
                "rejected_mean_error": 1.873923477642039,
                "gap_rejected_minus_accepted": 1.0103222197652948
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
      "best_epoch": 60,
      "best_calib_loss": 0.009590810164809227,
      "train_time_sec": 60.483909368515015,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9987547645192942,
            "spearman": 0.9973423344637677,
            "auroc_top30_bad": 0.999075380952381,
            "mae": 0.0433624453808974,
            "mse": 0.003446290359180162,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7657258919648031,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00545212322473526
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1984674234867096
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5747408802509308
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9272308301607768
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
            "pearson": 0.9986497547194141,
            "spearman": 0.9973963222638528,
            "auroc_top30_worst": 0.9991085714285715,
            "pairwise_seed_ranking": 0.9612,
            "predicted_best_mean_error": 1.530837094128132,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08477123388648033,
            "gap_to_oracle": 0.0019778599441051536,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6680973791480065
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8083631606340408
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0107258175730705
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2419458266178767
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.850841116905213,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057895697686407,
                "rejected_mean_error": 3.4556817440986634,
                "gap_rejected_minus_accepted": 2.0498921743300227
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0117228031158447,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2419458266178767,
                "rejected_mean_error": 2.717277668952942,
                "gap_rejected_minus_accepted": 1.4753318423350654
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4305846691131592,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0107258175730705,
                "rejected_mean_error": 2.2108317568302156,
                "gap_rejected_minus_accepted": 1.2001059392571451
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.049243837594986,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8083631606340408,
                "rejected_mean_error": 1.878250662724177,
                "gap_rejected_minus_accepted": 1.0698875020901362
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8949242115020755,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4107937186625268,
                "rejected_mean_error": 3.45893981218338,
                "gap_rejected_minus_accepted": 2.0481460935208533
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.044158935546875,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2435414383014043,
                "rejected_mean_error": 2.7318089971542356,
                "gap_rejected_minus_accepted": 1.4882675588528314
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4505168199539185,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.004477384388447,
                "rejected_mean_error": 2.2267392716407777,
                "gap_rejected_minus_accepted": 1.2222618872523308
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.048142910003662,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.8002234307527543,
                "rejected_mean_error": 1.8874032937685647,
                "gap_rejected_minus_accepted": 1.0871798630158105
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9811242522415826,
            "spearman": 0.9813427313336276,
            "auroc_top30_bad": 0.9872388571428572,
            "mae": 0.10075318873896467,
            "mse": 0.0221203882525627,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6984706981580736,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07556559962034226
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23917879526615143
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6804272965788841
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0361644552469254
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
            "pearson": 0.9787504986339284,
            "spearman": 0.9798596970622062,
            "auroc_top30_worst": 0.9854902857142858,
            "pairwise_seed_ranking": 0.8924,
            "predicted_best_mean_error": 1.4683725640773773,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06042125964164735,
            "gap_to_oracle": 0.005529541969299334,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8718314628601074
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9779487221668928
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1698102224349975
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3588558427814736
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.103896450996399,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4578781887690226,
                "rejected_mean_error": 2.244079917907715,
                "gap_rejected_minus_accepted": 0.7862017291386922
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9110642969608307,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3582411237307521,
                "rejected_mean_error": 2.070131051654633,
                "gap_rejected_minus_accepted": 0.7118899279238808
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.492018461227417,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1698102224349975,
                "rejected_mean_error": 1.9031865009307862,
                "gap_rejected_minus_accepted": 0.7333762784957887
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1253997385501862,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9785995209178986,
                "rejected_mean_error": 1.722861581703642,
                "gap_rejected_minus_accepted": 0.7442620607857433
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.123122763633728,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4530335410435995,
                "rejected_mean_error": 2.2106363677978518,
                "gap_rejected_minus_accepted": 0.7576028267542523
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9164288640022278,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3493872976558094,
                "rejected_mean_error": 2.0613179566368225,
                "gap_rejected_minus_accepted": 0.711930658981013
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.482176959514618,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1562238311767579,
                "rejected_mean_error": 1.9013638162612916,
                "gap_rejected_minus_accepted": 0.7451399850845337
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1274179220199585,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.961250208673023,
                "rejected_mean_error": 1.7199983571302444,
                "gap_rejected_minus_accepted": 0.7587481484572214
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9620220801566175,
            "spearman": 0.9691314653136531,
            "auroc_top30_bad": 0.987935238095238,
            "mae": 0.174855662855244,
            "mse": 0.07588245319037175,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6961453890333381,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09567321491241455
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21309663002490997
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.699874108016491
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0697957772493363
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
            "pearson": 0.9260897568328444,
            "spearman": 0.9536641526170578,
            "auroc_top30_worst": 0.984039619047619,
            "pairwise_seed_ranking": 0.926,
            "predicted_best_mean_error": 1.7265561369657516,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08059244441986091,
            "gap_to_oracle": 0.0026693367958068315,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9446966371536255
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1220250251965644
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.289895227432251
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4928886992082413
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.156107044219971,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.654062413321601,
                "rejected_mean_error": 3.138034154891968,
                "gap_rejected_minus_accepted": 1.4839717415703668
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9149061143398285,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4915549828886605,
                "rejected_mean_error": 2.733186790356621,
                "gap_rejected_minus_accepted": 1.2416318074679604
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5746482014656067,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.289895227432251,
                "rejected_mean_error": 2.3150239475250243,
                "gap_rejected_minus_accepted": 1.0251287200927732
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3120554983615875,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1233867608701078,
                "rejected_mean_error": 2.0293003502624902,
                "gap_rejected_minus_accepted": 0.9059135893923824
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1854862213134765,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.656051441695955,
                "rejected_mean_error": 3.1670228385925294,
                "gap_rejected_minus_accepted": 1.5109713968965743
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9363064169883728,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4973090534860438,
                "rejected_mean_error": 2.7268309895954435,
                "gap_rejected_minus_accepted": 1.2295219361093996
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5482070446014404,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2851280353069305,
                "rejected_mean_error": 2.3291691274642945,
                "gap_rejected_minus_accepted": 1.044041092157364
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.336908608675003,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.13033850940447,
                "rejected_mean_error": 2.0351648088445002,
                "gap_rejected_minus_accepted": 0.9048262994400302
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.990641433030131,
            "spearman": 0.988395468044455,
            "auroc_top30_bad": 0.9961542857142857,
            "mae": 0.09480003120445944,
            "mse": 0.016902521293367407,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7257924463500101,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07324043047428132
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20322708401679992
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5906389639854431
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9328207314809164
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
            "pearson": 0.9909492038757539,
            "spearman": 0.984147376222321,
            "auroc_top30_worst": 0.9976167619047619,
            "pairwise_seed_ranking": 0.9152,
            "predicted_best_mean_error": 1.5543913571834564,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06493092107772824,
            "gap_to_oracle": 0.0032480969429016238,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.572560430765152
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8755672953258722
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1183101456165314
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3099987347052295
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.578738927841188,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4742136016686758,
                "rejected_mean_error": 2.9621809310913085,
                "gap_rejected_minus_accepted": 1.4879673294226328
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9258724749088287,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3092272989332612,
                "rejected_mean_error": 2.562354438221112,
                "gap_rejected_minus_accepted": 1.2531271392878507
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4211273193359375,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1183101456165314,
                "rejected_mean_error": 2.1277105236053466,
                "gap_rejected_minus_accepted": 1.0094003779888152
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1139673590660095,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8768661800093545,
                "rejected_mean_error": 1.8722559273433788,
                "gap_rejected_minus_accepted": 0.9953897473340243
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5280386447906493,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4671877535184223,
                "rejected_mean_error": 2.988533000946045,
                "gap_rejected_minus_accepted": 1.5213452474276226
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.976536512374878,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2978753090542268,
                "rejected_mean_error": 2.5734585201929487,
                "gap_rejected_minus_accepted": 1.275583211138722
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4262499809265137,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1054411177635193,
                "rejected_mean_error": 2.13320343875885,
                "gap_rejected_minus_accepted": 1.0277623209953308
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.107718586921692,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8563410639762878,
                "rejected_mean_error": 1.8763694253197327,
                "gap_rejected_minus_accepted": 1.0200283613434449
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
      "best_epoch": 93,
      "best_calib_loss": 0.009287292137742043,
      "train_time_sec": 42.100186586380005,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.999470296351231,
            "spearman": 0.9986349830210715,
            "auroc_top30_bad": 0.9995257619047618,
            "mae": 0.022268952198131978,
            "mse": 0.0008510238772070495,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7460676018383396,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00014545537531375884
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19770093500614166
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5740622873306275
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9268822312831879
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
            "pearson": 0.9993700761179212,
            "spearman": 0.9991410875816433,
            "auroc_top30_worst": 0.9994980952380952,
            "pairwise_seed_ranking": 0.9686,
            "predicted_best_mean_error": 1.529607182651758,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08600114536285419,
            "gap_to_oracle": 0.0007479484677312964,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6654611499905586
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8070976805448532
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.010195270383358
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.241561130229632
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.757577919960022,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057152277297444,
                "rejected_mean_error": 3.4563508224487305,
                "gap_rejected_minus_accepted": 2.050635594718986
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.986647367477417,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.241561130229632,
                "rejected_mean_error": 2.7184317581176756,
                "gap_rejected_minus_accepted": 1.4768706278880435
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4249466061592102,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.010195270383358,
                "rejected_mean_error": 2.211362304019928,
                "gap_rejected_minus_accepted": 1.20116703363657
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.039909154176712,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8070976805448532,
                "rejected_mean_error": 1.8786724894205729,
                "gap_rejected_minus_accepted": 1.0715748088757198
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7821010351181035,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4107406090696653,
                "rejected_mean_error": 3.4594177985191346,
                "gap_rejected_minus_accepted": 2.048677189449469
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0094602704048157,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2435925418933234,
                "rejected_mean_error": 2.731655686378479,
                "gap_rejected_minus_accepted": 1.4880631444851555
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4389786124229431,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0040157027840615,
                "rejected_mean_error": 2.227200953245163,
                "gap_rejected_minus_accepted": 1.2231852504611016
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0303992331027985,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7987954264879227,
                "rejected_mean_error": 1.8878792951901753,
                "gap_rejected_minus_accepted": 1.0890838687022526
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9819985415919326,
            "spearman": 0.9806637822623311,
            "auroc_top30_bad": 0.9845706666666667,
            "mae": 0.10051493089082605,
            "mse": 0.021111388354764705,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6755981026398366,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05235791730880737
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23254703764915466
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6840010302901268
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.036793230398496
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
            "pearson": 0.9734577710394741,
            "spearman": 0.9722616777354738,
            "auroc_top30_worst": 0.9791725714285714,
            "pairwise_seed_ranking": 0.894,
            "predicted_best_mean_error": 1.4675572221279145,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06123660159111011,
            "gap_to_oracle": 0.0047142000198365785,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8840291662216186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9800621488919625
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1731564002990722
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3629979636115053
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.02751898765564,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4582377155092028,
                "rejected_mean_error": 2.240844177246094,
                "gap_rejected_minus_accepted": 0.7826064617368911
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8798130750656128,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3625256965610744,
                "rejected_mean_error": 2.0573047106258406,
                "gap_rejected_minus_accepted": 0.6947790140647663
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4896242022514343,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1731564002990722,
                "rejected_mean_error": 1.8998403230667114,
                "gap_rejected_minus_accepted": 0.7266839227676392
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1277177333831787,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9807532191657411,
                "rejected_mean_error": 1.7221421499516947,
                "gap_rejected_minus_accepted": 0.7413889307859536
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0038755416870115,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4529066446092394,
                "rejected_mean_error": 2.2117784357070924,
                "gap_rejected_minus_accepted": 0.7588717910978531
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8829440772533417,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3540934337014183,
                "rejected_mean_error": 2.0473489496443005,
                "gap_rejected_minus_accepted": 0.6932555159428822
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4902422428131104,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.162883388519287,
                "rejected_mean_error": 1.8947042589187622,
                "gap_rejected_minus_accepted": 0.7318208703994751
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1283701956272125,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9618783280962989,
                "rejected_mean_error": 1.719786744704221,
                "gap_rejected_minus_accepted": 0.7579084166079221
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9527074686938123,
            "spearman": 0.959815947549072,
            "auroc_top30_bad": 0.979439238095238,
            "mae": 0.1914433612786448,
            "mse": 0.10379613060874299,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6645461910200464,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09158743059635162
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20522805750370027
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6967307596087455
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0824140871604284
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
            "pearson": 0.8933252518887935,
            "spearman": 0.9433440692122044,
            "auroc_top30_worst": 0.9648487619047619,
            "pairwise_seed_ranking": 0.9264,
            "predicted_best_mean_error": 1.7259816788434983,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08116690254211423,
            "gap_to_oracle": 0.002094878673553513,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9480231766700744
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1177258166747215
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2903543458938598
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.5119444388570562
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 1.990679943561554,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.674456331782871,
                "rejected_mean_error": 2.9544888887405394,
                "gap_rejected_minus_accepted": 1.2800325569576685
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8077901601791382,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.5105220910197517,
                "rejected_mean_error": 2.67640666154246,
                "gap_rejected_minus_accepted": 1.1658845705227083
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5272393822669983,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2903543458938598,
                "rejected_mean_error": 2.3145648290634155,
                "gap_rejected_minus_accepted": 1.0242104831695558
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3086296617984772,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1189314705876117,
                "rejected_mean_error": 2.0307886169203573,
                "gap_rejected_minus_accepted": 0.9118571463327456
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 1.9905744671821595,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6916366798347897,
                "rejected_mean_error": 2.8467556953430178,
                "gap_rejected_minus_accepted": 1.155119015508228
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.80563086271286,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.508088542656465,
                "rejected_mean_error": 2.69483472808959,
                "gap_rejected_minus_accepted": 1.1867461854331252
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5193243026733398,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.287925206899643,
                "rejected_mean_error": 2.326371955871582,
                "gap_rejected_minus_accepted": 1.038446748971939
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3358405530452728,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.123365638274995,
                "rejected_mean_error": 2.037513957941596,
                "gap_rejected_minus_accepted": 0.9141483196666009
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9923617915085102,
            "spearman": 0.9910937799369063,
            "auroc_top30_bad": 0.9971710476190476,
            "mae": 0.08859837878725012,
            "mse": 0.01589222973352219,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6899900125706411,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.04732596689462662
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20005983951091766
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5887773049354553
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9330258893966675
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
            "pearson": 0.9909609884526795,
            "spearman": 0.9866595549821152,
            "auroc_top30_worst": 0.9988998095238095,
            "pairwise_seed_ranking": 0.9152,
            "predicted_best_mean_error": 1.5545462329387665,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06477604532241821,
            "gap_to_oracle": 0.0034029726982116593,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5687942097187042
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8760138823626897
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1172277765750884
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3093605543822369
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.437576580047608,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4746305554972754,
                "rejected_mean_error": 2.958428346633911,
                "gap_rejected_minus_accepted": 1.4837977911366356
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.918634831905365,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3085134420285485,
                "rejected_mean_error": 2.5644914475492775,
                "gap_rejected_minus_accepted": 1.255978005520729
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.420795500278473,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1172277765750884,
                "rejected_mean_error": 2.1287928926467896,
                "gap_rejected_minus_accepted": 1.0115651160717012
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1901617646217346,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8770134278570121,
                "rejected_mean_error": 1.8722067399620375,
                "gap_rejected_minus_accepted": 0.9951933121050254
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.402998948097229,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680864887767369,
                "rejected_mean_error": 2.980444383621216,
                "gap_rejected_minus_accepted": 1.5123578948444791
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9488309621810913,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2969041122472222,
                "rejected_mean_error": 2.5763412789692954,
                "gap_rejected_minus_accepted": 1.2794371667220732
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.439159631729126,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1037445635795593,
                "rejected_mean_error": 2.13489999294281,
                "gap_rejected_minus_accepted": 1.0311554293632508
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1865200996398926,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8600211928761194,
                "rejected_mean_error": 1.8751295957973297,
                "gap_rejected_minus_accepted": 1.0151084029212103
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
      "best_epoch": 120,
      "best_calib_loss": 0.009471001103520393,
      "train_time_sec": 56.14220666885376,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9981310800199175,
            "spearman": 0.9967015914569949,
            "auroc_top30_bad": 0.9990926904761904,
            "mae": 0.03804727423910024,
            "mse": 0.002998669241050526,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7449981393043474,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.020231794267892837
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19942628141641616
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5744080716133118
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9271969638824463
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
            "pearson": 0.9987302220583707,
            "spearman": 0.997706301164197,
            "auroc_top30_worst": 0.9993403809523809,
            "pairwise_seed_ranking": 0.9617,
            "predicted_best_mean_error": 1.530085973918438,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08552235409617426,
            "gap_to_oracle": 0.0012267397344112307,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6686523005366325
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8082039979219436
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0108675496935844
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2416115864356359
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7594614505767834,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057675376666916,
                "rejected_mean_error": 3.455880033016205,
                "gap_rejected_minus_accepted": 2.0501124953495133
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9798072278499603,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2416115864356359,
                "rejected_mean_error": 2.718280389499664,
                "gap_rejected_minus_accepted": 1.4766688030640283
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4159314036369324,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0108675496935844,
                "rejected_mean_error": 2.2106900247097014,
                "gap_rejected_minus_accepted": 1.199822475016117
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.049841821193695,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8082039979219436,
                "rejected_mean_error": 1.8783037169615429,
                "gap_rejected_minus_accepted": 1.0700997190395993
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.790065431594849,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4107406090696653,
                "rejected_mean_error": 3.4594177985191346,
                "gap_rejected_minus_accepted": 2.048677189449469
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.999788910150528,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2433343587319057,
                "rejected_mean_error": 2.732430235862732,
                "gap_rejected_minus_accepted": 1.4890958771308263
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4305091500282288,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0046628170609475,
                "rejected_mean_error": 2.226553838968277,
                "gap_rejected_minus_accepted": 1.2218910219073296
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0421492159366608,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7995074404478073,
                "rejected_mean_error": 1.8876419572035472,
                "gap_rejected_minus_accepted": 1.08813451675574
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9825569774707013,
            "spearman": 0.9807362236231517,
            "auroc_top30_bad": 0.9853866666666667,
            "mae": 0.10583404090206748,
            "mse": 0.020537940821044324,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6806996573832252,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07853622925281524
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.23566042149066926
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6822526831030845
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0352008887847264
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
            "pearson": 0.9621272246610266,
            "spearman": 0.9659128388562169,
            "auroc_top30_worst": 0.9783923809523809,
            "pairwise_seed_ranking": 0.884,
            "predicted_best_mean_error": 1.4688364703655243,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.059957353353500276,
            "gap_to_oracle": 0.00599344825744641,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9246089272499084
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9845860397968537
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.172829983139038
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3626731815876991
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0429935216903687,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4569078110588922,
                "rejected_mean_error": 2.252813317298889,
                "gap_rejected_minus_accepted": 0.7959055062399969
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8709739446640015,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3622011614202054,
                "rejected_mean_error": 2.0582762423414773,
                "gap_rejected_minus_accepted": 0.6960750809212719
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5208719372749329,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.172829983139038,
                "rejected_mean_error": 1.9001667402267457,
                "gap_rejected_minus_accepted": 0.7273367570877076
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1205728650093079,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9856269641425282,
                "rejected_mean_error": 1.7205141006691607,
                "gap_rejected_minus_accepted": 0.7348871365266325
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.042165470123291,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.450623671743605,
                "rejected_mean_error": 2.232325191497803,
                "gap_rejected_minus_accepted": 0.7817015197541979
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8734601438045502,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.353578176727907,
                "rejected_mean_error": 2.0488783632005965,
                "gap_rejected_minus_accepted": 0.6953001864726895
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.532821536064148,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1626833238601684,
                "rejected_mean_error": 1.8949043235778809,
                "gap_rejected_minus_accepted": 0.7322209997177125
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.114963173866272,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.967063169630747,
                "rejected_mean_error": 1.718039979909193,
                "gap_rejected_minus_accepted": 0.750976810278446
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9639243609208273,
            "spearman": 0.9735792619045207,
            "auroc_top30_bad": 0.9870041904761906,
            "mae": 0.1894014592273936,
            "mse": 0.0785474956658908,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6718263574524412,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.09291585719585418
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.22413315575122833
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7010929549098015
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.051642423303922
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
            "pearson": 0.9367221498074207,
            "spearman": 0.9449784787062265,
            "auroc_top30_worst": 0.9867062857142856,
            "pairwise_seed_ranking": 0.9284,
            "predicted_best_mean_error": 1.7258943070173263,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08125427436828625,
            "gap_to_oracle": 0.0020075068473814905,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9429908123016357
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.140030718002564
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2904467489242553
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4618838195607606
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.197324895858765,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.651522900475396,
                "rejected_mean_error": 3.1608897705078123,
                "gap_rejected_minus_accepted": 1.5093668700324163
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.933729112148285,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.46132243888228,
                "rejected_mean_error": 2.8236912431808325,
                "gap_rejected_minus_accepted": 1.3623688042985524
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.6091279983520508,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2904467489242553,
                "rejected_mean_error": 2.31447242603302,
                "gap_rejected_minus_accepted": 1.0240256771087646
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.308044284582138,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1403256239601598,
                "rejected_mean_error": 2.0236420107244046,
                "gap_rejected_minus_accepted": 0.8833163867642448
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1953529596328734,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.651319750547409,
                "rejected_mean_error": 3.2096080589294433,
                "gap_rejected_minus_accepted": 1.5582883083820342
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9633225500583649,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.4572090501772528,
                "rejected_mean_error": 2.8458579835437594,
                "gap_rejected_minus_accepted": 1.3886489333665066
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5978904366493225,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.288028722524643,
                "rejected_mean_error": 2.326268440246582,
                "gap_rejected_minus_accepted": 1.0382397177219391
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3059789836406708,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1564358241028256,
                "rejected_mean_error": 2.026372665389974,
                "gap_rejected_minus_accepted": 0.8699368412871484
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9914053117904302,
            "spearman": 0.9900115667834407,
            "auroc_top30_bad": 0.997240380952381,
            "mae": 0.08526002243053189,
            "mse": 0.014435339655651918,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.701687752671634,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05679445880651474
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1978980617046356
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5912554839134216
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9327256741841634
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
            "pearson": 0.9895802880796042,
            "spearman": 0.9867485693110845,
            "auroc_top30_worst": 0.9981287619047619,
            "pairwise_seed_ranking": 0.91,
            "predicted_best_mean_error": 1.5547002665996552,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06462201166152948,
            "gap_to_oracle": 0.0035570063591003898,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5736290056705475
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8686713458826909
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.117144849061966
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.309197001778749
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4937336921691897,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4757613741821713,
                "rejected_mean_error": 2.9482509784698485,
                "gap_rejected_minus_accepted": 1.4724896042876772
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9386310577392578,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3084544808849325,
                "rejected_mean_error": 2.5646679542316035,
                "gap_rejected_minus_accepted": 1.256213473346671
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.468656837940216,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.117144849061966,
                "rejected_mean_error": 2.1288758201599123,
                "gap_rejected_minus_accepted": 1.0117309710979463
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2147668302059174,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8700630204936567,
                "rejected_mean_error": 1.874528487565805,
                "gap_rejected_minus_accepted": 1.0044654670721482
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.468295383453369,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4684279624621073,
                "rejected_mean_error": 2.9773711204528808,
                "gap_rejected_minus_accepted": 1.5089431579907735
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9557430148124695,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.296801249929928,
                "rejected_mean_error": 2.5766466004507884,
                "gap_rejected_minus_accepted": 1.2798453505208605
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4811758995056152,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1037289652824402,
                "rejected_mean_error": 2.1349155912399294,
                "gap_rejected_minus_accepted": 1.0311866259574891
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.2117050290107727,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8529051400366283,
                "rejected_mean_error": 1.8775269825828267,
                "gap_rejected_minus_accepted": 1.0246218425461984
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
      "best_epoch": 95,
      "best_calib_loss": 0.008578171953558922,
      "train_time_sec": 55.476911544799805,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9997196574694815,
            "spearman": 0.9989331914474106,
            "auroc_top30_bad": 0.9998045238095239,
            "mae": 0.015466792576484511,
            "mse": 0.0004884552666642014,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7452407760920255,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.00029336635768413544
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.19768980555534363
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5739391874074936
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.926716226943334
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
            "pearson": 0.9996291192311966,
            "spearman": 0.9993944970397363,
            "auroc_top30_worst": 0.999843238095238,
            "pairwise_seed_ranking": 0.9605,
            "predicted_best_mean_error": 1.5300865505337715,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.08552177748084078,
            "gap_to_oracle": 0.0012273163497447115,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6662978009581566
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8072338709115982
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0101016418337823
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2413006339947383
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.7944239616394047,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.405716653631793,
                "rejected_mean_error": 3.456337989330292,
                "gap_rejected_minus_accepted": 2.050621335698499
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9833959639072418,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2413006339947383,
                "rejected_mean_error": 2.719213246822357,
                "gap_rejected_minus_accepted": 1.4779126128276188
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4085795283317566,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0101016418337823,
                "rejected_mean_error": 2.211455932569504,
                "gap_rejected_minus_accepted": 1.2013542907357215
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0245681405067444,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8072338709115982,
                "rejected_mean_error": 1.878627092631658,
                "gap_rejected_minus_accepted": 1.0713932217200597
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8291391849517824,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.4107309549715783,
                "rejected_mean_error": 3.4595046854019165,
                "gap_rejected_minus_accepted": 2.048773730430338
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0010260343551636,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2431144967476526,
                "rejected_mean_error": 2.733089821815491,
                "gap_rejected_minus_accepted": 1.4899753250678383
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4170907139778137,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0037886319756508,
                "rejected_mean_error": 2.2274280240535735,
                "gap_rejected_minus_accepted": 1.2236393920779227
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0234289169311523,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7991397255659103,
                "rejected_mean_error": 1.8877645288308462,
                "gap_rejected_minus_accepted": 1.088624803264936
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.983278328809944,
            "spearman": 0.9839510759751178,
            "auroc_top30_bad": 0.9896380952380952,
            "mae": 0.09574099581751823,
            "mse": 0.01947126403736896,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6820785421811258,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0690776042342186
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2361497143983841
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6795723417639732
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0335975264469783
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
            "pearson": 0.977874249063665,
            "spearman": 0.9798672849070624,
            "auroc_top30_worst": 0.9880289523809523,
            "pairwise_seed_ranking": 0.8916,
            "predicted_best_mean_error": 1.4671970076560974,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06159681606292722,
            "gap_to_oracle": 0.004353985548019468,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.8992590427398681
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9812914859025906
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1693896081924438
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.358852956594943
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.045064973831177,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.455103160964118,
                "rejected_mean_error": 2.2690551681518554,
                "gap_rejected_minus_accepted": 0.8139520071877373
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8867572844028473,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3581389810893936,
                "rejected_mean_error": 2.0704368269100737,
                "gap_rejected_minus_accepted": 0.7122978458206801
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.520138680934906,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1693896081924438,
                "rejected_mean_error": 1.9036071151733398,
                "gap_rejected_minus_accepted": 0.734217506980896
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0995176136493683,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.982271069535813,
                "rejected_mean_error": 1.721635119892108,
                "gap_rejected_minus_accepted": 0.739364050356295
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.037731099128723,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4498331620958116,
                "rejected_mean_error": 2.239439778327942,
                "gap_rejected_minus_accepted": 0.7896066162321305
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8880002796649933,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3493381955406882,
                "rejected_mean_error": 2.0614637041848805,
                "gap_rejected_minus_accepted": 0.7121255086441922
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5241222381591797,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.157593955039978,
                "rejected_mean_error": 1.8999936923980714,
                "gap_rejected_minus_accepted": 0.7423997373580933
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0964440405368805,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9662905666563246,
                "rejected_mean_error": 1.718300268611806,
                "gap_rejected_minus_accepted": 0.7520097019554814
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9611826301559602,
            "spearman": 0.9688574749882435,
            "auroc_top30_bad": 0.984783619047619,
            "mae": 0.18291672444790444,
            "mse": 0.08509022037956185,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6732162007563586,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.08937632828950882
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.21027399413585662
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.7001673728823662
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0635976863145828
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
            "pearson": 0.917227468283377,
            "spearman": 0.946450274848176,
            "auroc_top30_worst": 0.9756708571428572,
            "pairwise_seed_ranking": 0.936,
            "predicted_best_mean_error": 1.725778890967369,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08136969041824349,
            "gap_to_oracle": 0.0018920907974242507,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9379450845718383
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1179038691215026
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2947129524230958
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4840882991168545
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0962694883346566,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6560778819190132,
                "rejected_mean_error": 3.1198949375152587,
                "gap_rejected_minus_accepted": 1.4638170555962455
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8779493570327759,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.483724431141718,
                "rejected_mean_error": 2.7566284101230267,
                "gap_rejected_minus_accepted": 1.2729039789813088
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5993942022323608,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2947129524230958,
                "rejected_mean_error": 2.3102062225341795,
                "gap_rejected_minus_accepted": 1.0154932701110837
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.321450561285019,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1188114275947547,
                "rejected_mean_error": 2.0308287166607673,
                "gap_rejected_minus_accepted": 0.9120172890660125
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.1040646553039553,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6584376556343503,
                "rejected_mean_error": 3.1455469131469727,
                "gap_rejected_minus_accepted": 1.4871092575126224
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8775912523269653,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.477243712719749,
                "rejected_mean_error": 2.786390016949366,
                "gap_rejected_minus_accepted": 1.3091463042296168
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.59696763753891,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.2871544988155366,
                "rejected_mean_error": 2.3271426639556885,
                "gap_rejected_minus_accepted": 1.039988165140152
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3341172337532043,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.1322488193474118,
                "rejected_mean_error": 2.034521228489391,
                "gap_rejected_minus_accepted": 0.9022724091419794
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9913240965799064,
            "spearman": 0.9897565632447886,
            "auroc_top30_bad": 0.9980449523809524,
            "mae": 0.08564316889810587,
            "mse": 0.014979159415551686,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7065927361102321,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.07547162288427353
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20297288603782654
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5889325240135193
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9326591435750325
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
            "pearson": 0.9928099963190375,
            "spearman": 0.9906245756317285,
            "auroc_top30_worst": 0.9990552380952381,
            "pairwise_seed_ranking": 0.9068,
            "predicted_best_mean_error": 1.554715902328491,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06460637593269358,
            "gap_to_oracle": 0.003572642087936284,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.5761727969646454
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8702562253635663
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.114888440179825
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3090783514257178
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.4411466598510763,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.474945381614897,
                "rejected_mean_error": 2.9555949115753175,
                "gap_rejected_minus_accepted": 1.4806495299604205
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9805935323238373,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3082309378949148,
                "rejected_mean_error": 2.5653371548119446,
                "gap_rejected_minus_accepted": 1.2571062169170297
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4557462930679321,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.114888440179825,
                "rejected_mean_error": 2.1311322290420533,
                "gap_rejected_minus_accepted": 1.0162437888622284
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.193497359752655,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8714429015359177,
                "rejected_mean_error": 1.8740675454460316,
                "gap_rejected_minus_accepted": 1.0026246439101139
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.396721315383911,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680441996786329,
                "rejected_mean_error": 2.9808249855041504,
                "gap_rejected_minus_accepted": 1.5127807858255176
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9809479415416718,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2969628524652776,
                "rejected_mean_error": 2.576166923083956,
                "gap_rejected_minus_accepted": 1.2792040706186785
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4667723774909973,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1029942784309388,
                "rejected_mean_error": 2.135650278091431,
                "gap_rejected_minus_accepted": 1.032655999660492
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1909205913543701,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.853170997566647,
                "rejected_mean_error": 1.8774374156074727,
                "gap_rejected_minus_accepted": 1.0242664180408256
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
      "best_epoch": 95,
      "best_calib_loss": 0.008730724453926086,
      "train_time_sec": 60.5827214717865,
      "metrics": {
        "train": {
          "all_candidate": {
            "n": 10000,
            "pearson": 0.9991423274569883,
            "spearman": 0.9979066463386664,
            "auroc_top30_bad": 0.9993742857142858,
            "mae": 0.03206653447329154,
            "mse": 0.0019115280586784003,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.999,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.7552507350206925,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.000716733917593956
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.1988079207956791
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5743553381681442
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9271652426083883
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
            "pearson": 0.9990115940487562,
            "spearman": 0.9982910922195615,
            "auroc_top30_worst": 0.9994270476190475,
            "pairwise_seed_ranking": 0.9622,
            "predicted_best_mean_error": 1.5315695900321007,
            "seed0_mean_error": 1.6156083280146123,
            "random_seed_mean_error": 1.6104893134832383,
            "oracle_best_mean_error": 1.5288592341840268,
            "improvement_over_seed0": 0.0840387379825116,
            "gap_to_oracle": 0.0027103558480738865,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.6676438396573067
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8080329414129257
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.0104100464224814
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.2415942350625992
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.610778787201643
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.8141742229461673,
                "accepted_n": 4500,
                "rejected_n": 500,
                "accepted_mean_error": 1.4057047311133808,
                "rejected_mean_error": 3.456445291996002,
                "gap_rejected_minus_accepted": 2.0507405608826215
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.006547510623932,
                "accepted_n": 3750,
                "rejected_n": 1250,
                "accepted_mean_error": 1.2415942350625992,
                "rejected_mean_error": 2.7183324436187744,
                "gap_rejected_minus_accepted": 1.476738208556175
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.432056188583374,
                "accepted_n": 2500,
                "rejected_n": 2500,
                "accepted_mean_error": 1.0104100464224814,
                "rejected_mean_error": 2.2111475279808044,
                "gap_rejected_minus_accepted": 1.200737481558323
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0515101552009583,
                "accepted_n": 1250,
                "rejected_n": 3750,
                "accepted_mean_error": 0.8080329414129257,
                "rejected_mean_error": 1.878360735797882,
                "gap_rejected_minus_accepted": 1.0703277943849563
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.831629133224488,
                "accepted_n": 900,
                "rejected_n": 100,
                "accepted_mean_error": 1.41073055177927,
                "rejected_mean_error": 3.4595083141326906,
                "gap_rejected_minus_accepted": 2.0487777623534207
              },
              {
                "reject_rate": 0.25,
                "threshold": 2.0271615386009216,
                "accepted_n": 750,
                "rejected_n": 250,
                "accepted_mean_error": 1.2434529894590378,
                "rejected_mean_error": 2.7320743436813353,
                "gap_rejected_minus_accepted": 1.4886213542222975
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4453153014183044,
                "accepted_n": 500,
                "rejected_n": 500,
                "accepted_mean_error": 1.0039564335942268,
                "rejected_mean_error": 2.2272602224349978,
                "gap_rejected_minus_accepted": 1.223303788840771
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.0456028282642365,
                "accepted_n": 250,
                "rejected_n": 750,
                "accepted_mean_error": 0.7993697165250778,
                "rejected_mean_error": 1.8876878651777904,
                "gap_rejected_minus_accepted": 1.0883181486527125
              }
            ]
          }
        },
        "calib": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9828256073158705,
            "spearman": 0.9824925471372,
            "auroc_top30_bad": 0.986887619047619,
            "mae": 0.09809296333347374,
            "mse": 0.020105277827748184,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6965598275499391,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.05441880905628204
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.24530894501209258
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6805245675444603
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0349356905221938
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
            "pearson": 0.9776590261721929,
            "spearman": 0.978309448134047,
            "auroc_top30_worst": 0.9856457142857142,
            "pairwise_seed_ranking": 0.902,
            "predicted_best_mean_error": 1.4671298034191131,
            "seed0_mean_error": 1.5287938237190246,
            "random_seed_mean_error": 1.537072078704834,
            "oracle_best_mean_error": 1.462843022108078,
            "improvement_over_seed0": 0.06166402029991147,
            "gap_to_oracle": 0.004286781311035215,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.88695529794693
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.9793890168269476
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.170417636680603
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.3599172520485006
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.5364983616828918
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.0901227951049806,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.4567934014002482,
                "rejected_mean_error": 2.2538430042266846,
                "gap_rejected_minus_accepted": 0.7970496028264364
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9053833484649658,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3592621767406403,
                "rejected_mean_error": 2.067074416925351,
                "gap_rejected_minus_accepted": 0.7078122401847107
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4950510263442993,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.170417636680603,
                "rejected_mean_error": 1.9025790866851806,
                "gap_rejected_minus_accepted": 0.7321614500045777
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1229957342147827,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.9803025848187578,
                "rejected_mean_error": 1.7222926820227786,
                "gap_rejected_minus_accepted": 0.7419900972040209
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.073480153083801,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.450405806965298,
                "rejected_mean_error": 2.2342859745025634,
                "gap_rejected_minus_accepted": 0.7838801675372653
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8944522440433502,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.3515511081817952,
                "rejected_mean_error": 2.0548952174565147,
                "gap_rejected_minus_accepted": 0.7033441092747195
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4959654808044434,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.1594644155502318,
                "rejected_mean_error": 1.8981232318878174,
                "gap_rejected_minus_accepted": 0.7386588163375856
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1229957342147827,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.9634972735056802,
                "rejected_mean_error": 1.7192413245930391,
                "gap_rejected_minus_accepted": 0.755744051087359
              }
            ]
          }
        },
        "test_id": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9585610908613271,
            "spearman": 0.9662756378859648,
            "auroc_top30_bad": 0.9855459047619048,
            "mae": 0.1753934595949184,
            "mse": 0.08791802762854663,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 0.996,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.6794137915673047,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.0952985686659813
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.20933634085655212
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.6952828966975212
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.0755815212806066
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
            "pearson": 0.9156163636269441,
            "spearman": 0.9588250606240388,
            "auroc_top30_worst": 0.976295619047619,
            "pairwise_seed_ranking": 0.9316,
            "predicted_best_mean_error": 1.7257598766088487,
            "seed0_mean_error": 1.8071485813856125,
            "random_seed_mean_error": 1.8040734711885453,
            "oracle_best_mean_error": 1.7238868001699448,
            "improvement_over_seed0": 0.08138870477676385,
            "gap_to_oracle": 0.0018730764389038868,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.9464573192596436
              },
              {
                "coverage": 0.25,
                "mean_true_error": 1.1134585592991266
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.2915719690322875
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.4975583333450595
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.8024595874786378
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.087690591812134,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.6633431496090358,
                "rejected_mean_error": 3.0545075283050536,
                "gap_rejected_minus_accepted": 1.3911643786960177
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8674969375133514,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.4970986491969709,
                "rejected_mean_error": 2.7165912142196023,
                "gap_rejected_minus_accepted": 1.2194925650226314
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5499879121780396,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.2915719690322875,
                "rejected_mean_error": 2.313347205924988,
                "gap_rejected_minus_accepted": 1.0217752368927004
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.347367137670517,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 1.1140868480974875,
                "rejected_mean_error": 2.0324069379869623,
                "gap_rejected_minus_accepted": 0.9183200898894748
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.10192551612854,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.6701950739489662,
                "rejected_mean_error": 3.0397301483154298,
                "gap_rejected_minus_accepted": 1.3695350743664636
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.8775741457939148,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.5020641335510314,
                "rejected_mean_error": 2.7127167043231784,
                "gap_rejected_minus_accepted": 1.210652570772147
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.5241793990135193,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.284541056394577,
                "rejected_mean_error": 2.329756106376648,
                "gap_rejected_minus_accepted": 1.0452150499820712
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.3767793476581573,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 1.113516721933607,
                "rejected_mean_error": 2.040832042056609,
                "gap_rejected_minus_accepted": 0.9273153201230018
              }
            ]
          }
        },
        "test_ood": {
          "all_candidate": {
            "n": 2500,
            "pearson": 0.9908046104568098,
            "spearman": 0.9891347473959875,
            "auroc_top30_bad": 0.9961020952380952,
            "mae": 0.09070505044033197,
            "mse": 0.016133808496222504,
            "expert_lt_perturb_large": 1.0,
            "expert_lt_other_task": 1.0,
            "expert_lt_simvla_seed0": 1.0,
            "same_context_pred_std": 0.722002334506546,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.06216160619258881
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.2024533885717392
              },
              {
                "coverage": 0.5,
                "mean_true_error": 0.5898357258796691
              },
              {
                "coverage": 0.75,
                "mean_true_error": 0.9330076999664306
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
            "pearson": 0.9910861232506603,
            "spearman": 0.9845486103991108,
            "auroc_top30_worst": 0.99776,
            "pairwise_seed_ranking": 0.9204,
            "predicted_best_mean_error": 1.5536479539871215,
            "seed0_mean_error": 1.6193222782611847,
            "random_seed_mean_error": 1.626927037715912,
            "oracle_best_mean_error": 1.5511432602405548,
            "improvement_over_seed0": 0.06567432427406317,
            "gap_to_oracle": 0.0025046937465666996,
            "risk_coverage": [
              {
                "coverage": 0.1,
                "mean_true_error": 0.570622083902359
              },
              {
                "coverage": 0.25,
                "mean_true_error": 0.8735105980856296
              },
              {
                "coverage": 0.5,
                "mean_true_error": 1.1195280834674834
              },
              {
                "coverage": 0.75,
                "mean_true_error": 1.310197946391126
              },
              {
                "coverage": 1.0,
                "mean_true_error": 1.623010334610939
              }
            ],
            "switch_proxy_all_simvla": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5948088645935066,
                "accepted_n": 1125,
                "rejected_n": 125,
                "accepted_mean_error": 1.474855956421958,
                "rejected_mean_error": 2.9563997383117675,
                "gap_rejected_minus_accepted": 1.4815437818898094
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9476503133773804,
                "accepted_n": 937,
                "rejected_n": 313,
                "accepted_mean_error": 1.3093766530333613,
                "rejected_mean_error": 2.561907330260109,
                "gap_rejected_minus_accepted": 1.252530677226748
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4019396901130676,
                "accepted_n": 625,
                "rejected_n": 625,
                "accepted_mean_error": 1.1195280834674834,
                "rejected_mean_error": 2.1264925857543946,
                "gap_rejected_minus_accepted": 1.0069645022869111
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1415203213691711,
                "accepted_n": 313,
                "rejected_n": 937,
                "accepted_mean_error": 0.8745815004594029,
                "rejected_mean_error": 1.873019112721324,
                "gap_rejected_minus_accepted": 0.9984376122619212
              }
            ],
            "switch_proxy_seed0": [
              {
                "reject_rate": 0.1,
                "threshold": 2.5364994049072265,
                "accepted_n": 225,
                "rejected_n": 25,
                "accepted_mean_error": 1.4680441996786329,
                "rejected_mean_error": 2.9808249855041504,
                "gap_rejected_minus_accepted": 1.5127807858255176
              },
              {
                "reject_rate": 0.25,
                "threshold": 1.9825640618801117,
                "accepted_n": 187,
                "rejected_n": 63,
                "accepted_mean_error": 1.2986115819630137,
                "rejected_mean_error": 2.5712730752097235,
                "gap_rejected_minus_accepted": 1.2726614932467097
              },
              {
                "reject_rate": 0.5,
                "threshold": 1.4117392301559448,
                "accepted_n": 125,
                "rejected_n": 125,
                "accepted_mean_error": 1.106330952167511,
                "rejected_mean_error": 2.1323136043548585,
                "gap_rejected_minus_accepted": 1.0259826521873474
              },
              {
                "reject_rate": 0.75,
                "threshold": 1.1362468004226685,
                "accepted_n": 63,
                "rejected_n": 187,
                "accepted_mean_error": 0.8551569145823282,
                "rejected_mean_error": 1.876768363350853,
                "gap_rejected_minus_accepted": 1.0216114487685246
              }
            ]
          }
        }
      }
    }
  ]
}
```
