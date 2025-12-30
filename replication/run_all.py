import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")

scripts = [
    "setup.py",
    "preprocessing.py",
    "transformations.py",
    "descriptive_analysis.py",

    "model_estimation.py",
    "policy_interactions.py",
    "lagged_models.py",
    "diagnostics.py",
    "robustness_checks.py",

    "sector_descriptives.py",
    "pre_post_reforms.py",
    "macro_correlation.py",
    "sector_trends.py",
    "policy_coefficient_plot.py",

    "export_results.py"
]

for script in scripts:
    path = os.path.join(SRC_DIR, script)

    if not os.path.exists(path):
        print(f"ERROR: Missing script -> {script}")
        sys.exit(1)

    exit_code = os.system(f'python "{path}"')

    if exit_code != 0:
        print(f"ERROR: Script failed -> {script}")
        sys.exit(1)

print("FULL PIPELINE EXECUTED SUCCESSFULLY")
