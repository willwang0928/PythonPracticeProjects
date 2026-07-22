# Portfolio Analyzer

Extends the single-stock analyzer to a multi-stock, weighted portfolio, in
plain Python (no pandas/numpy).

## What it does

- Loads daily price data for multiple tickers (`AAPL`, `GOOG`, `MSFT`)
- Computes each ticker's daily returns
- Combines them into a single weighted portfolio return series
- Computes portfolio volatility
- Computes pairwise Pearson correlation between every pair of tickers
- Prints a summary report: portfolio weights, average portfolio return,
  portfolio volatility, and a correlation matrix

## How to run

```bash
cd 02_portfolio_analyzer
python3 portfolio_analyzer.py
```

## Sample output

```
***********Generating report***********
Tickers included: ['AAPL', 'MSFT', 'GOOG']
Weight of each stock in portfolio: {'AAPL': 0.5, 'MSFT': 0.3, 'GOOG': 0.2}
The average portfolio daily return is -0.001607120669958802.
The portfolio volatility is 0.008693924462209702.
Correlation matrix:
  AAPL-GOOG: -0.0007465925553391294
  AAPL-MSFT: 0.05030596603009668
  GOOG-MSFT: -0.04383663574026967
```

## Concepts demonstrated

- Loading and aggregating data across multiple files into a single portfolio
- Weighted sums across dictionaries keyed by ticker
- Covariance / correlation from scratch
- Reusable, importable module design — this file's functions
  (`load_ticker`, `load_all`, `daily_returns`, `all_daily_returns`,
  `portfolio_return`, `covariance`, `correlation`) are imported directly by
  Projects 4 and 5 rather than reimplemented.
