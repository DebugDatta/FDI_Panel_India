import sys
import numpy as np
import pandas as pd
from setup import DATA_PATH, log

df = pd.read_csv(DATA_PATH).set_index(["Sector","Year"])

if (df["FDI_USD_Mn"] < 0).any():
    log("NEGATIVE FDI VALUES")
    sys.exit(1)

df["ln_FDI_check"] = np.log(df["FDI_USD_Mn"] + 1)

if (df["ln_FDI"] - df["ln_FDI_check"]).abs().max() > 1e-6:
    log("LN_FDI MISMATCH")
    sys.exit(1)

for v in ["GDP_Growth","Inflation","Exchange_Rate","Repo_Rate"]:
    df[f"{v}_lag1"] = df.groupby(level=0)[v].shift(1)

df = df.dropna()

df.to_csv(DATA_PATH)
log("TRANSFORMATIONS OK")
