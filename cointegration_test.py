import pandas as pd
from statsmodels.tsa.stattools import coint

#Load the data
df = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

#Pick two assets (KO and PEP)
x = df["KO"]
y = df["PEP"]

#Perform the cointegration test
score, pvalue, _ = coint(x, y)

#Print the results
print(f"Cointegration test between KO and PEP:")
print(f"Test Statistic: {score}")
print(f"P-value: {pvalue:.4f}")

#Interpret
if pvalue < 0.05:
    print("The pair is likely cointegrated (p < 0.05).")
else:
    print("No cointegration detected (p ≥ 0.05).")
