1 # MISSION: The 100-Experiment TDQC Marathon
    2
    3 You are the Master Orchestrator (Maestro) for the TDQC VLA Calibration project. Your mission is to implement, test, and orchestrate 100 distinct experiment blueprints, culminating in a robust,
      automated pipeline ready for a massive 1000-epoch training marathon.
    4
    5 ## 📁 Workspace & Boundaries
    6 - **Target Directory:** `/media/redafrix/My Passport/reda_ws/intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/`
    7 - **Rule:** EVERYTHING must be contained within this directory. Copy base scripts, core library files, and generate any new datasets directly inside this folder. Do not pollute the parent
      directories.
    8
    9 ## 🧠 The Ideas
   10 Read the following file to understand the 100 ideas:
   11 `intern_ship_ws/tdqc/code/phase2_tdqc_standalone/experiments/a_100_tests/the_ideas.md`
   12 You must implement a unique training/model script variant for **each** of the 100 ideas. Be smart and adapt the architecture appropriately for each idea. 
   13
   14 ## 📊 Data Constraints
   15 - **Base Data:** Strictly use the `v8` dataset splits (`v8_train.pt`, `v8_val.pt`, `v8_test.pt`, `v8_unseen_obj_ood.pt`).
   16 - **Data Modification:** Some ideas (e.g., Delta-Only inputs) require changing what the model sees. You must write scripts to generate these modified datasets from the base `v8` data and save them
      in the target directory. Ensure the pipeline correctly points to these modified datasets for the relevant tests.
   17
   18 ## ⚙️ Training & Evaluation Standards
   19 - **Epochs:** Ultimately, every test will run for exactly **1000 epochs** with **NO early stopping**.
   20 - **Granular Evaluation:** At the end of a training run, you must execute an exhaustive evaluation on both the **Test** and **OOD** datasets.
   21 - **Metrics Required:** Accuracy, Brier Score, AUC-ROC, and Sample Count (N).
   22 - **Sequence Steps Required:** 10, 20, 50, 100, 150, 200, 300, and Overall (Max-Pooling proactivity logic).
   23 - **Plotting:** Generate relevant plots (e.g., Loss curves, Brier curves) for each run.
   24
   25 ## 🚀 Orchestration & Analysis
   26 - **The Cascade:** Write a robust master orchestration script (bash or python). It must run the 100 tests back-to-back, ideally launching each in an isolated sub-shell or process. **Crucially: If
      one test crashes, the orchestrator MUST catch the error, log it, and seamlessly start the next test.**
   27 - **The Final Ranker:** Write a post-processing script that runs after all 100 tests are complete. It must parse all results, rank the experiments based on their granular Brier/AUC scores, and
      output a final summary report determining the best ideas.
   28
   29 ## 🛠️ EXECUTION PLAN (Follow Strictly)
   30
   31 You must use your specialized sub-agents (`coder`, `ml_engineer`, `debugger`, `devops_engineer`) to execute this in phases:
   32
   33 ### Phase 1: Implementation & Setup
   34 1. Create the `a_100_tests` directory structure.
   35 2. Implement the 100 model/training variants based on the MD file.
   36 3. Write the data-generation scripts for modified inputs.
   37 4. Write the granular evaluation script.
   38 5. Write the robust Master Orchestrator script and the Final Ranker script.
   39 6. *Optional:* Update `/media/redafrix/My Passport/reda_ws/GEMINI.md` to document this new 100-test protocol if you feel it's necessary for future context.
   40
   41 ### Phase 2: The Smoke Test (1 Epoch)
   42 1. Configure ALL 100 training scripts to run for exactly **1 epoch**.
   43 2. Run the Master Orchestrator. 
   44
   45 ### Phase 3: Iterative Debugging
   46 1. Review the logs from the smoke test.
   47 2. For any test that crashed or threw an error, use the `debugger` and `coder` agents to fix the code, fix the tensor shapes, or fix the environment. Create specific python environments if a test
      requires conflicting dependencies.
   48 3. Rerun the failed smoke tests until **100% of the tests complete successfully**.
   49
   50 ### Phase 4: Production Readiness
   51 1. Once all tests pass the 1-epoch smoke test perfectly, **DELETE** all generated checkpoints, logs, and plots from the smoke test.
   52 2. Reconfigure all 100 training scripts to their final state: **1000 epochs**.
   53 3. Stop and report to me. I will manually launch the final marathon.
   54
   55 **Do not ask for permission to proceed through the phases; work autonomously until Phase 4 is complete or you are completely stuck.**

  ---


