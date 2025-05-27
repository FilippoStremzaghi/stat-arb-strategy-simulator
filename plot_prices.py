import pandas as pd
import matplotlib.pyplot as plt

# Load the saved prices
df = pd.read_csv("prices.csv", index_col=0, parse_dates=True)

# Plot the prices
plt.figure(figsize=(12, 6))
plt.plot(df["KO"], label="KO (Coca-Cola)")
plt.plot(df["PEP"], label="PEP (Pepsi)")

plt.title("Daily Closing Prices: KO vs. PEP")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
