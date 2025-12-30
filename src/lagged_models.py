import pandas as pd
from linearmodels.panel import PanelOLS
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH).set_index(["Sector", "Year"])

y = df["ln_FDI"]
X = df[
    [
        "GDP_Growth_lag1",
        "Exchange_Rate_lag1",
        "Inflation_lag1",
        "Repo_Rate_lag1"
    ]
]

res = PanelOLS(
    y,
    X,
    entity_effects=True,
    time_effects=False
).fit(cov_type="clustered", cluster_entity=True)

with open(f"{OUTPUT_TABLES}/Table_4_Lagged_Macro_Response.csv", "w") as f:
    f.write(res.summary.tables[1].as_csv())

log("LAGGED MACRO RESPONSE MODEL OK")
