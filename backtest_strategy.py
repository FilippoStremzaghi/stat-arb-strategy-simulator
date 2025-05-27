import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load price data
df = pd.read_csv("prices.csv", index_col=0, parse_dates=True)
ko = df["KO"]
pep = df["PEP"]

# Daily returns
ko_ret = ko.pct_change().fillna(0)
pep_ret = pep.pct_change().fillna(0)

# Spread and z-score
spread = ko - pep
zscore = (spread - spread.mean()) / spread.std()

# Initialize lists
position = 0   # 1 = long KO / short PEP, -1 = short KO / long PEP, 0 = no position
entry_price_ko = 0
entry_price_pep = 0
trades = []

returns = []

for t in range(1, len(df)):
    date = df.index[t]
    z = zscore.iloc[t]

    # ENTRY: Long KO / Short PEP
    if position == 0 and z < -1.0:
        position = 1
        entry_price_ko = ko.iloc[t]
        entry_price_pep = pep.iloc[t]
        entry_date = date

    # ENTRY: Short KO / Long PEP
    elif position == 0 and z > 1.0:
        position = -1
        entry_price_ko = ko.iloc[t]
        entry_price_pep = pep.iloc[t]
        entry_date = date

    # EXIT: Close Position
    elif position != 0 and abs(z) < 0.5:
        exit_price_ko = ko.iloc[t]
        exit_price_pep = pep.iloc[t]

        # Calculate trade return
        if position == 1:
            ret = (exit_price_ko / entry_price_ko - 1) - (exit_price_pep / entry_price_pep - 1)
        elif position == -1:
            ret = (entry_price_ko / exit_price_ko - 1) - (entry_price_pep / exit_price_pep - 1)

        trades.append({
            "Entry Date": entry_date,
            "Exit Date": date,
            "Position": "Long KO / Short PEP" if position == 1 else "Short KO / Long PEP",
            "Return": ret
        })

        returns.append(ret)
        position = 0  # Reset position

# Convert to DataFrame
trades_df = pd.DataFrame(trades)

# Compute performance
total_return = np.prod([1 + r for r in returns]) - 1
sharpe = np.mean(returns) / np.std(returns) * np.sqrt(252) if len(returns) > 1 else 0
max_drawdown = np.max(np.maximum.accumulate(np.cumprod([1 + r for r in returns])) - np.cumprod([1 + r for r in returns]))

# Display results
print("\n📊 Backtest Summary")
print(f"Total Trades: {len(trades)}")
print(f"Total Return: {total_return:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")

# Plot cumulative return
cumulative = np.cumprod([1 + r for r in returns])
plt.figure(figsize=(10, 5))
plt.plot(cumulative, label="Cumulative Return")
plt.title("Backtest: Pairs Trading KO/PEP")
plt.xlabel("Trade #")
plt.ylabel("Return")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



# Save trades to CSV
trades_df.to_csv("trades.csv", index=False)
print("\n📁 Saved trade log to 'trades.csv'")
