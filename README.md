### My first project in pyhton ###
# Statistical Arbitrage Strategy Simulator

This project implements a simple pairs trading strategy using Coca-Cola (KO) and Pepsi (PEP) stock prices. It uses a mean-reverting approach based on the spread's z-score and simulates entry/exit trades.

## Strategy Logic
- Calculate price spread between KO and PEP
- Enter long (KO) / short (PEP) when z-score < -1
- Enter short (KO) / long (PEP) when z-score > +1
- Exit all positions when z-score returns to ~0

## Skills Used
- Python, Pandas, NumPy, Matplotlib
- Statistical testing (`statsmodels.coint`)
- Data fetching with Yahoo Finance
- Backtesting logic & performance analysis

## Key Metrics (Example Output)
- Total Return: XX%
- Sharpe Ratio: X.XX
- Max Drawdown: XX%
- Trades Executed: XX

## 📂 Files
- `download_stocks.py`: Get price data
- `plot_prices.py`: Visualize time series
- `visualize_spread.py`: Z-score & spread
- `backtest_strategy.py`: Run backtest and track performance
- `trades.csv`: Trade log output