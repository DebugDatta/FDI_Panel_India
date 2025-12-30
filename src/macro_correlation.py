import pandas as pd
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH)

macro_vars = [
    "GDP_Growth",
    "Inflation",
    "Exchange_Rate",
    "Repo_Rate"
]

corr = df[macro_vars].corr()
corr.to_csv(f"{OUTPUT_TABLES}/Appendix_Table_A4_Macro_Correlations.csv")

log("MACRO CORRELATION TABLE OK")
