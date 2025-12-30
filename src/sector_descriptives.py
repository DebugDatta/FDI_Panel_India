import pandas as pd
from setup import DATA_PATH, OUTPUT_TABLES, log

df = pd.read_csv(DATA_PATH)

sector_stats = (
    df.groupby("Sector")["FDI_USD_Mn"]
      .agg(["mean", "std", "min", "max", "sum"])
      .rename(columns={
          "mean": "Mean_FDI",
          "std": "Std_FDI",
          "min": "Min_FDI",
          "max": "Max_FDI",
          "sum": "Total_FDI"
      })
)

sector_stats["FDI_Share_Percent"] = (
    sector_stats["Total_FDI"] / sector_stats["Total_FDI"].sum() * 100
)

sector_stats.to_csv(f"{OUTPUT_TABLES}/Appendix_Table_A2_Sector_FDI_Summary.csv")

log("SECTOR DESCRIPTIVES OK")
