# Moving-Average Crossover Backtester

A simple trend-following strategy backtest, in plain Python (no pandas/numpy).

## What it does

- Loads daily closing prices for `AAPL.csv`
- Computes a fast (5-day) and slow (20-day) SMA
- Generates a long/flat position signal: long when fast SMA > slow SMA, flat
  otherwise
- Simulates an equity curve starting from $10,000 by applying daily returns
  only while the position is long
- Reports:
  - Total strategy return vs. buy-and-hold return
  - Number of trades (position changes)
  - Daily and annualized Sharpe ratio
  - Max drawdown (chronological running-peak method, not global max − global
    min)

## How to run

```bash
cd 03_ma_crossover_backtester
python3 backtester.py
```

## Sample output

```
******Generating report******
Total return: -0.016285554935862274
This is how many times your strategy traded: 2
Buy-and-hold total return: -0.13720425663808244
The daily and annual Sharpe ratios are -0.040039339524294525 (daily) and -0.6356048102433751 (annual)
The max drawdown is 0.04426984557030636
```

## Concepts demonstrated

- Rolling-window SMA calculations for two different window sizes and
  aligning series of different lengths
- Signal generation from a crossover rule
- Equity curve simulation via compounding
- Sharpe ratio (daily → annualized) and running-peak max drawdown, both
  reused and extended in later projects
