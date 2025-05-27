import yfinance as yf
import pandas as pd

tickers = ["KO", "PEP"]
print("Downloading data...")

# Download data
data = yf.download(tickers, start="2018-01-01", end="2023-12-31")

print("\nDownload complete.")
print("\nData shape:", data.shape)
print("\nColumn structure:\n", data.columns)

if isinstance(data.columns, pd.MultiIndex):
    close_prices = data.xs('Close', level=0, axis=1)
else:
    close_prices = data[['Close']]

print("\n Close Prices Preview:\n", close_prices.head())

# Save to file
close_prices.to_csv("prices.csv")
print(" Saved to prices.csv")

