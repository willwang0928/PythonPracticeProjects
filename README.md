# Python Practice Projects — Quant-Flavored Python Fluency Curriculum

Five small, self-contained projects, each building on the last, written in
plain Python — no `pandas`, no `numpy`. The goal was fluency with core Python
(functions, dictionaries, list comprehensions, and eventually classes)
through the lens of quantitative finance: returns, volatility, correlation,
backtesting, Monte Carlo simulation, and factor regression.

Each project's `README.md` has its own details, sample output, and run
instructions. This file gives the overview.

## Projects

| # | Project | Highlights |
|---|---------|------------|
| 1 | [Stock Data Analyzer](01_stock_data_analyzer) | Single-stock returns, SMA, volatility from a CSV |
| 2 | [Portfolio Analyzer](02_portfolio_analyzer) | Multi-stock weighted portfolio returns, volatility, pairwise correlation |
| 3 | [MA Crossover Backtester](03_ma_crossover_backtester) | Fast/slow SMA crossover strategy, equity curve, Sharpe, max drawdown |
| 4 | [Monte Carlo Simulator](04_monte_carlo_simulator) | 1,000-trial random-walk simulation of portfolio outcomes, VaR |
| 5 | [CAPM / Risk Report](05_capm_risk_report) | OOP `Portfolio` class, manual CAPM regression (beta/alpha) vs. a benchmark |

## Progression

The projects build in a deliberate order:

1. **Project 1** establishes the fundamentals — reading a CSV, computing
   returns, a moving average, and volatility for one stock.
2. **Project 2** generalizes that to a weighted, multi-stock portfolio, and
   introduces covariance/correlation. Its functions (`load_all`,
   `all_daily_returns`, `portfolio_return`, `covariance`, `correlation`)
   become a reusable module imported directly by Projects 4 and 5, rather
   than being reimplemented.
3. **Project 3** turns those return series into an actual trading strategy:
   a moving-average crossover backtest with an equity curve, Sharpe ratio,
   and a chronological (running-peak) max drawdown calculation.
4. **Project 4** shifts from historical analysis to forward-looking
   simulation: using the portfolio's historical mean/volatility to generate
   1,000 random future paths and characterize the outcome distribution
   (median, best/worst case, 5% VaR, probability of loss).
5. **Project 5** is the first object-oriented project: a `Portfolio` class
   wraps volatility, Sharpe, and max drawdown as methods over shared
   instance state, and adds a manual least-squares CAPM regression
   (beta/alpha per stock vs. a benchmark).

## Requirements

Plain Python 3, standard library only (`csv`, `math`, `random`). No external
dependencies.

## What's next

The next planned iteration is revisiting all five projects using `pandas`
and `numpy`, to compare the hand-rolled implementations here against
vectorized, library-based equivalents.
