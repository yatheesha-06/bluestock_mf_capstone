import requests
import pandas as pd
from pathlib import Path

SCHEMES = {
    "HDFC_Top100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

OUTPUT = Path("data/raw")

for name, code in SCHEMES.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"Fetching {name}")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            OUTPUT / f"{name}_live_nav.csv",
            index=False
        )

        print(f"Saved {name}")

    else:
        print(f"Failed {name}")