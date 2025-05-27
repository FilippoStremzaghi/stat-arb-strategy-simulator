import pandas as pd
import matplotlib.pyplot as plt

# Load the price data
df = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

# Extract the two series
ko = df["KO"]
pep = df["PEP"]

# Step 1: Calculate the spread (KO - PEP)
spread = ko - pep

# Step 2: Calculate the z-score of the spread
zscore = (spread - spread.mean()) / spread.std()

# Step 3: Plot the spread and z-score
plt.figure(figsize=(14, 6))

# Subplot 1: Spread
plt.subplot(2, 1, 1)
plt.plot(spread, label="Spread (KO - PEP)")
plt.axhline(spread.mean(), color="black", linestyle="--", label="Mean")
plt.axhline(spread.mean() + spread.std(), color="red", linestyle="--", label="+1 Std Dev")
plt.axhline(spread.mean() - spread.std(), color="green", linestyle="--", label="-1 Std Dev")
plt.legend()
plt.title("Spread Between KO and PEP")

# Subplot 2: Z-score
plt.subplot(2, 1, 2)
plt.plot(zscore, label="Z-score of Spread")
plt.axhline(1, color="red", linestyle="--")
plt.axhline(-1, color="green", linestyle="--")
plt.axhline(0, color="black", linestyle="--")
plt.legend()
plt.title("Z-score of Spread (Mean Reversion Signal)")

plt.tight_layout()
plt.show()
