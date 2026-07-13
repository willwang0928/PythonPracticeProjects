# Project 2: Multi-Stock Portfolio Analyzer (Plain Python — no pandas/numpy)
#
# Goal: extend Project 1 to work across several stocks at once and treat
# them as a weighted portfolio. Main goal is still Python fluency —
# nested data structures, looping over multiple data sources, writing
# your own math instead of reaching for a library. The quant angle
# (portfolio return, correlation) is just the vehicle.
#
# Data: this folder should have one CSV per ticker, e.g.
#   AAPL.csv, MSFT.csv, GOOG.csv
# each with the same columns as Project 1: date, open, high, low, close, volume
# Assume all CSVs cover the exact same dates in the exact same order
# (no need to handle misaligned dates for this project).
#
# What your script should do:
#
# 1. Load each CSV into some data structure keyed by ticker, e.g.
#      { "AAPL": {"dates": [...], "closes": [...]}, "MSFT": {...}, ... }
#    Write one function that loads a single CSV (reuse it per ticker
#    rather than copy-pasting the loading logic).
#
# 2. Compute the daily returns for each ticker (same formula as Project 1:
#    (close_today - close_yesterday) / close_yesterday).
#
# 3. Given a dict of portfolio weights, e.g.
#      weights = {"AAPL": 0.5, "MSFT": 0.3, "GOOG": 0.2}
#    compute the portfolio's daily return for each day as the
#    weighted sum of that day's individual stock returns:
#      port_return[day] = sum(weights[t] * returns[t][day] for t in tickers)
#
# 4. Compute the portfolio's average daily return and volatility
#    (std dev of the portfolio daily returns — write this yourself,
#    no numpy, same as Project 1).
#
# 5. Compute the pairwise correlation between each pair of tickers'
#    daily returns. Write the Pearson correlation formula yourself:
#      corr(X, Y) = covariance(X, Y) / (stdev(X) * stdev(Y))
#    where covariance(X, Y) = average of (x_i - mean(X)) * (y_i - mean(Y))
#
# 6. Print a summary report with:
#    - the tickers included and their weights
#    - the average portfolio daily return
#    - the portfolio volatility
#    - a correlation table/matrix between every pair of tickers
#
# Notes:
# - Structure this as functions (e.g. load_ticker, compute_returns,
#   portfolio_returns, portfolio_volatility, correlation, main) rather
#   than one long script.
# - Try to reuse your Project 1 logic conceptually, but it's fine (and
#   good practice) to rewrite it fresh here rather than importing it.
# - Think about the data structure for "returns per ticker" before you
#   start looping — it'll make steps 3 and 5 much easier.
# - Ping for help if you get stuck on something specific — not for the
#   full answer, just to talk through the blocker.

import csv

def main():
    print(load_all(['AAPL', 'GOOG', 'MSFT']))

def load_ticker(filename):
    l = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            l.append(row)
    return l

def load_all(tickers):
    l = {}
    for ticker in tickers:
        l[ticker] = load_ticker(ticker + '.csv')
    return l
    
    
    
if __name__ == "__main__":
    main()