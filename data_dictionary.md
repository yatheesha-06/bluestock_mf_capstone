# Data Dictionary

## 01_fund_master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Scheme Name |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |

Source: 01_fund_master.csv

---

## 02_nav_history

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Fund Code |
| date | Date | NAV Date |
| nav | Decimal | Net Asset Value |

Source: 02_nav_history.csv

---

## 03_aum_by_fund_house

| Column | Data Type | Description |
|----------|----------|----------|
| date | Date | Reporting Date |
| fund_house | Text | AMC Name |
| aum_lakh_crore | Decimal | Assets Under Management (Lakh Crore) |
| aum_crore | Integer | Assets Under Management (Crore) |

Source: 03_aum_by_fund_house.csv