import sys
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH)

X = df[["GDP_Growth","Inflation","Exchange_Rate","Repo_Rate"]]

if X.shape[0] <= X.shape[1]:
    log("INSUFFICIENT OBSERVATIONS FOR VIF")
    sys.exit(1)

vif = pd.DataFrame({"Variable": X.columns, "VIF": [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]})
vif.to_csv(f"{OUTPUT_TABLES}/VIF_Diagnostics.csv", index=False)

log("DIAGNOSTICS OK")
