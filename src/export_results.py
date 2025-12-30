import os
import pandas as pd
from setup import OUTPUT_TABLES, log

files = sorted(os.listdir(OUTPUT_TABLES))

if not files:
    log("NO TABLES FOUND")
    raise SystemExit

pd.DataFrame({"Generated_Tables": files}).to_csv(f"{OUTPUT_TABLES}/Tables_Index.csv", index=False)
log("EXPORT OK")
