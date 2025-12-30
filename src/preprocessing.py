import sys
import pandas as pd
from setup import DATA_PATH, log

df = pd.read_csv(DATA_PATH)

required = ["Sector","Year","FDI_USD_Mn","ln_FDI","GDP_Growth","Inflation","Exchange_Rate","Repo_Rate","GST_2017","TaxCut_2019","PLI_2020"]
missing = set(required) - set(df.columns)

if missing:
    log(f"MISSING COLUMNS {missing}")
    sys.exit(1)

df = df.dropna()
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df = df.dropna(subset=["Year"])

df = df.set_index(["Sector","Year"]).sort_index()

if df.index.duplicated().any():
    log("DUPLICATE PANEL KEYS")
    sys.exit(1)

df.to_csv(DATA_PATH)
log("PREPROCESSING OK")
