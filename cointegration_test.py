import pandas as pd
from statsmodels.tsa.stattools import coint

# Step 1: Load the data
df = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

# Step 2: Pick two assets (KO and PEP)
x = df["KO"]
y = df["PEP"]

# Step 3: Perform the cointegration test
score, pvalue, _ = coint(x, y)

# Step 4: Print the results
print(f"Cointegration test between KO and PEP:")
print(f"Test Statistic: {score}")
print(f"P-value: {pvalue:.4f}")

# Step 5: Interpret
if pvalue < 0.05:
    print("✅ The pair is likely cointegrated (p < 0.05).")
else:
    print("❌ No cointegration detected (p ≥ 0.05).")
