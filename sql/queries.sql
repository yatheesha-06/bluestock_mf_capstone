

SELECT scheme_name, aum_crore
FROM 07_scheme_performance_clean
ORDER BY aum_crore DESC
LIMIT 5;


SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM 02_nav_history_clean
GROUP BY amfi_code
ORDER BY avg_nav DESC;


SELECT state,
       COUNT(*) AS total_transactions
FROM 08_investor_transactions_clean
GROUP BY state
ORDER BY total_transactions DESC;

SELECT scheme_name,
       expense_ratio_pct
FROM 07_scheme_performance_clean
WHERE expense_ratio_pct < 1;



SELECT category,
       AVG(return_3yr_pct) AS avg_3yr_return
FROM 07_scheme_performance_clean
GROUP BY category
ORDER BY avg_3yr_return DESC;



SELECT investor_id,
       SUM(amount_inr) AS total_amount
FROM 08_investor_transactions_clean
GROUP BY investor_id
ORDER BY total_amount DESC
LIMIT 10;


SELECT kyc_status,
       COUNT(*) AS total_count
FROM 08_investor_transactions_clean
GROUP BY kyc_status;



SELECT fund_house,
       COUNT(*) AS total_schemes
FROM 01_fund_master_clean
GROUP BY fund_house
ORDER BY total_schemes DESC;


SELECT fund_house,
       AVG(sharpe_ratio) AS avg_sharpe
FROM 07_scheme_performance_clean
GROUP BY fund_house
ORDER BY avg_sharpe DESC;


SELECT category,
       SUM(net_inflow_crore) AS total_inflow
FROM 05_category_inflows_clean
GROUP BY category
ORDER BY total_inflow DESC;