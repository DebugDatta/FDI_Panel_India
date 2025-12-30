import pandas as pd
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH)

reforms = {
    "GST_2017": 2017,
    "TaxCut_2019": 2019,
    "PLI_2020": 2020
}

rows = []

for policy, year in reforms.items():
    pre = df[df["Year"] < year].groupby("Sector")["ln_FDI"].mean()
    post = df[df["Year"] >= year].groupby("Sector")["ln_FDI"].mean()
    diff = post - pre

    temp = pd.DataFrame({
        "Policy": policy,
        "Pre_Reform_Mean_lnFDI": pre,
        "Post_Reform_Mean_lnFDI": post,
        "Difference": diff
    })

    rows.append(temp.reset_index())

out = pd.concat(rows, ignore_index=True)
out.to_csv(f"{OUTPUT_TABLES}/Appendix_Table_A3_Pre_Post_Reform_Means.csv", index=False)

log("PRE-POST REFORM DESCRIPTIVES OK")
