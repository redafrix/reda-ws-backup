# Git State

## Commit
a27a06d2ca74d0e987a5e552e01013073e93cfd8

## Remote
origin	https://github.com/hzxie/DynamicVLA.git (fetch)
origin	https://github.com/hzxie/DynamicVLA.git (push)

## Status
 M scripts/replay_dataset_seq.py
 M scripts/translate_dataset_seq.py
?? scripts/replay_dataset_seq.py.bak_stage3_translate_fix
?? scripts/translate_dataset_seq.py.bak_stage3_translate_fix

## Diff stat
 scripts/replay_dataset_seq.py    | 1 -
 scripts/translate_dataset_seq.py | 1 -
 2 files changed, 2 deletions(-)

## Full diff
diff --git a/scripts/replay_dataset_seq.py b/scripts/replay_dataset_seq.py
index 0750ee8..448f1f9 100644
--- a/scripts/replay_dataset_seq.py
+++ b/scripts/replay_dataset_seq.py
@@ -95,7 +95,6 @@ def main(args):
         args.scene_dir,
         args.object_dir,
         args.physics_time_step,
-        args.timeout,
         args.tolerance,
         args.device,
         args.disable_fabric,
diff --git a/scripts/translate_dataset_seq.py b/scripts/translate_dataset_seq.py
index 6987098..2cd0ad7 100644
--- a/scripts/translate_dataset_seq.py
+++ b/scripts/translate_dataset_seq.py
@@ -248,7 +248,6 @@ def main(args):
             args.scene_dir,
             args.object_dir,
             args.physics_time_step,
-            args.timeout,
             args.tolerance,
             args.device,
             args.disable_fabric,
