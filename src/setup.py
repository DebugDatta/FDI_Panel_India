import os
import sys
import numpy as np
from datetime import datetime

np.random.seed(42)

BASE_DIR = os.getcwd()
DATA_PATH = os.path.join(BASE_DIR, "data", "final_panel_dataset.csv")

OUTPUT_TABLES = os.path.join(BASE_DIR, "outputs", "tables")
OUTPUT_FIGURES = os.path.join(BASE_DIR, "outputs", "figures")
OUTPUT_LOGS = os.path.join(BASE_DIR, "outputs", "logs")

os.makedirs(OUTPUT_TABLES, exist_ok=True)
os.makedirs(OUTPUT_FIGURES, exist_ok=True)
os.makedirs(OUTPUT_LOGS, exist_ok=True)

LOG_FILE = os.path.join(OUTPUT_LOGS, "pipeline.log")

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | {msg}\n")

if not os.path.exists(DATA_PATH):
    log("DATA FILE NOT FOUND")
    sys.exit(1)

log("SETUP OK")
