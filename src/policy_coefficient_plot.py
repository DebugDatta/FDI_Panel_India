import pandas as pd
import matplotlib.pyplot as plt
from setup import OUTPUT_TABLES, OUTPUT_FIGURES, log

path = f"{OUTPUT_TABLES}/Table_3_Policy_Interactions.csv"

table = pd.read_csv(
    path,
    skiprows=1,
    header=None
)

table.columns = [
    "Term",
    "Coefficient",
    "StdErr",
    "Tstat",
    "Pvalue",
    "LowerCI",
    "UpperCI"
]

# Drop non-coefficient rows
table = table[table["Term"].notna()]

# Convert numeric columns explicitly
num_cols = ["Coefficient", "StdErr", "Tstat", "Pvalue", "LowerCI", "UpperCI"]
for c in num_cols:
    table[c] = pd.to_numeric(table[c], errors="coerce")

# Drop rows where conversion failed
table = table.dropna(subset=["Coefficient", "LowerCI", "UpperCI"])

# Keep only policy interaction terms
table = table[
    table["Term"].str.contains("GST_2017|TaxCut_2019|PLI_2020", regex=True)
]

table = table.sort_values("Coefficient")

plt.figure(figsize=(8, 12))
plt.errorbar(
    table["Coefficient"],
    table["Term"],
    xerr=[
        table["Coefficient"] - table["LowerCI"],
        table["UpperCI"] - table["Coefficient"]
    ],
    fmt="o"
)

plt.axvline(0, linestyle="--")
plt.xlabel("Estimated Coefficient")
plt.title("Sector-wise Policy Interaction Effects")
plt.tight_layout()

plt.savefig(f"{OUTPUT_FIGURES}/Figure_2_Policy_Coefficient_Plot.png")
plt.close()

log("POLICY COEFFICIENT PLOT OK")
