import pandas as pd
from pathlib import Path


raw_path = Path("data/raw")
processed_path = Path("data/processed")

processed_path.mkdir(exist_ok=True)

fund_master = pd.read_csv(raw_path / "01_fund_master.csv")

fund_master["launch_date"] = pd.to_datetime(
    fund_master["launch_date"]
)

fund_master = fund_master.drop_duplicates()

fund_master.to_csv(
    processed_path / "01_fund_master_clean.csv",
    index=False
)

print("✓ fund_master cleaned")


nav = pd.read_csv(raw_path / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    processed_path / "02_nav_history_clean.csv",
    index=False
)

print("✓ nav_history cleaned")


aum = pd.read_csv(
    raw_path / "03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"]
)

aum = aum.drop_duplicates()

aum.to_csv(
    processed_path /
    "03_aum_by_fund_house_clean.csv",
    index=False
)

print("✓ aum data cleaned")


sip = pd.read_csv(
    raw_path / "04_monthly_sip_inflows.csv"
)

sip = sip.drop_duplicates()

sip.to_csv(
    processed_path /
    "04_monthly_sip_inflows_clean.csv",
    index=False
)

print("✓ sip inflows cleaned")


category = pd.read_csv(
    raw_path / "05_category_inflows.csv"
)

category = category.drop_duplicates()

category.to_csv(
    processed_path /
    "05_category_inflows_clean.csv",
    index=False
)

print("✓ category inflows cleaned")


folios = pd.read_csv(
    raw_path / "06_industry_folio_count.csv"
)

folios = folios.drop_duplicates()

folios.to_csv(
    processed_path /
    "06_industry_folio_count_clean.csv",
    index=False
)

print("✓ industry folios cleaned")


perf = pd.read_csv(
    raw_path / "07_scheme_performance.csv"
)

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf = perf.drop_duplicates()

perf.to_csv(
    processed_path /
    "07_scheme_performance_clean.csv",
    index=False
)

print("✓ scheme performance cleaned")


txn = pd.read_csv(
    raw_path / "08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"]
    .isin(valid_types)
]

txn = txn[
    txn["amount_inr"] > 0
]

txn = txn.drop_duplicates()

txn.to_csv(
    processed_path /
    "08_investor_transactions_clean.csv",
    index=False
)

print("✓ investor transactions cleaned")


holdings = pd.read_csv(
    raw_path / "09_portfolio_holdings.csv"
)

holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"]
)

holdings = holdings.drop_duplicates()

holdings.to_csv(
    processed_path /
    "09_portfolio_holdings_clean.csv",
    index=False
)

print("✓ portfolio holdings cleaned")

benchmark = pd.read_csv(
    raw_path / "10_benchmark_indices.csv"
)

benchmark["date"] = pd.to_datetime(
    benchmark["date"]
)

benchmark = benchmark.drop_duplicates()

benchmark.to_csv(
    processed_path /
    "10_benchmark_indices_clean.csv",
    index=False
)

print("✓ benchmark indices cleaned")

print("\nALL DATASETS CLEANED SUCCESSFULLY")