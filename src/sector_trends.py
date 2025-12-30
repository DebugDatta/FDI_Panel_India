import pandas as pd
import matplotlib.pyplot as plt
from setup import DATA_PATH, OUTPUT_FIGURES, log

df = pd.read_csv(DATA_PATH)

sectors = df["Sector"].unique()

for s in sectors:
    temp = df[df["Sector"] == s]

    plt.figure()
    plt.plot(temp["Year"], temp["ln_FDI"])
    plt.title(f"FDI Trend: {s}")
    plt.xlabel("Year")
    plt.ylabel("ln(FDI)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_FIGURES}/FDI_Trend_{s}.png")
    plt.close()

log("SECTOR TRENDS OK")
