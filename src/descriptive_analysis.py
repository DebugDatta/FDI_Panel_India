import sys
import pandas as pd
import matplotlib.pyplot as plt
from setup import DATA_PATH, OUTPUT_TABLES, OUTPUT_FIGURES, log

df = pd.read_csv(DATA_PATH)

if df.empty:
    log("EMPTY DATASET")
    sys.exit(1)

df.describe().to_csv(f"{OUTPUT_TABLES}/Appendix_Table_A1.csv")

fdi = df.groupby("Year")["FDI_USD_Mn"].sum()

if fdi.empty:
    log("FDI SERIES EMPTY")
    sys.exit(1)

fdi.plot()
plt.tight_layout()
plt.savefig(f"{OUTPUT_FIGURES}/Figure_A1_FDI_Trends.png")
plt.close()

log("DESCRIPTIVES OK")
