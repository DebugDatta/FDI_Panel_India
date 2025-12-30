import pandas as pd
from linearmodels.panel import PanelOLS
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH).set_index(["Sector", "Year"])

policies = ["GST_2017", "TaxCut_2019", "PLI_2020"]
sectors = df.index.get_level_values(0).unique()

interaction_cols = []

for p in policies:
    for s in sectors:
        col = f"{s}_{p}"
        df[col] = (df.index.get_level_values(0) == s).astype(int) * df[p]
        interaction_cols.append(col)

y = df["ln_FDI"]
X = df[["GDP_Growth", "Exchange_Rate"] + interaction_cols]

res = PanelOLS(
    y,
    X,
    entity_effects=True,
    time_effects=False
).fit(cov_type="clustered", cluster_entity=True)

with open(f"{OUTPUT_TABLES}/Table_3_Policy_Interactions.csv", "w") as f:
    f.write(res.summary.tables[1].as_csv())

log("SECTOR–POLICY INTERACTION MODEL OK")
