import pandas as pd
from linearmodels.panel import PanelOLS
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH).set_index(["Sector", "Year"])

y = df["ln_FDI"]
X = df[["GDP_Growth", "Exchange_Rate"]]

res = PanelOLS(
    y,
    X,
    entity_effects=True,
    time_effects=False
).fit(cov_type="clustered", cluster_entity=True)

with open(f"{OUTPUT_TABLES}/Table_2_Macro_Sensitivity.csv", "w") as f:
    f.write(res.summary.tables[1].as_csv())

log("BASELINE MACRO SENSITIVITY MODEL OK")
