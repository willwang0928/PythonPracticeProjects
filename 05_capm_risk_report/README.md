# CAPM / Factor Regression + Risk Report

An object-oriented risk report for a multi-stock portfolio, in plain Python
(no pandas/numpy). The first OOP project in this series — prior projects were
all function-based.

## What it does

- A `Portfolio` class holds tickers, weights, per-ticker daily returns,
  weighted portfolio returns, and benchmark (SPY) returns as instance state,
  loaded once in `__init__` via Project 2's `portfolio_analyzer` module
- `volatility()` — standard deviation of portfolio daily returns
- `sharpe()` — daily and annualized Sharpe ratio
- `max_drawdown()` — builds a compounded equity curve from the portfolio's
  daily returns, then walks it with a running-peak algorithm to find the
  largest peak-to-trough decline
- `beta_alpha(ticker)` — manual least-squares CAPM regression of a given
  stock's returns against the SPY benchmark: `beta = cov(x, y) / var(x)`,
  `alpha = mean(y) - beta * mean(x)`

Note: `SPY.csv` in this folder is synthetic benchmark data (correlated with
the existing AAPL/GOOG/MSFT returns), generated for this exercise since no
real S&P 500 data was available in the repo.

## How to run

```bash
cd 05_capm_risk_report
python3 risk_report.py
```

## Sample output

```
The portfolio's volatility is 0.008693924462209702
The portfolio's Sharpe ratio is (-0.18485560542244767, -2.9344917624244773)
The portfolio's max drawdown is 0.13285654081617435
AAPL's beta/alpha is (1.256566701323727, -0.001350378687712574)
MSFT's beta/alpha is (1.0591427852026671, 0.0002177180460683529)
GOOG's beta/alpha is (1.5293323854610106, 0.00018089734524248842)
```

## Concepts demonstrated

- Object-oriented design: state (`self.*` attributes) computed once and
  reused across methods, instead of re-passing/reloading data on every call
- Building an equity curve from percentage returns before running a
  drawdown calculation (drawdown must be computed on compounded dollar
  values, not raw returns)
- Manual linear regression (CAPM beta/alpha) without a stats library
