from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

processed_path = Path("data/processed")

for file in processed_path.glob("*.csv"):

    df = pd.read_csv(file)

    table_name = file.stem

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table_name} : {len(df)} rows"
    )

print("\nDATABASE LOADED SUCCESSFULLY")