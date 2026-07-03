"""Runtime helper for LIBERO-PRO goal-object OOD BDDL aliasing.

Use only if your benchmark registry says problem_folder='libero_goal_object_ood'
but your BDDL files live in bddl_files/libero_goal_object_ood_temp.

Example:
    task = alias_goal_object_ood_task(task)
    env, task_description = get_libero_env(task, ...)
"""

def alias_goal_object_ood_task(task):
    if getattr(task, "problem_folder", None) != "libero_goal_object_ood":
        return task
    if hasattr(task, "_replace"):
        return task._replace(problem_folder="libero_goal_object_ood_temp")
    try:
        task.problem_folder = "libero_goal_object_ood_temp"
        return task
    except Exception:
        import copy
        task2 = copy.copy(task)
        object.__setattr__(task2, "problem_folder", "libero_goal_object_ood_temp")
        return task2
