# Stock Data Analyzer

A single-stock analysis tool built in plain Python (no pandas/numpy). Reads daily
OHLC price data from a CSV and reports core descriptive statistics.

## What it does

- Loads daily closing prices and dates from `data.csv`
- Computes daily returns
- Computes a 5-day simple moving average (SMA)
- Computes volatility (standard deviation of daily returns)
- Prints a summary report: date range, average daily return, volatility, and
  the most recent SMA value

## How to run

```bash
cd 01_stock_data_analyzer
python3 analyzer.py
```

## Sample output

```
***********Generating report***********
Date range: 2026-01-02 - 2026-03-26
The average daily return is 0.001342860281315648
The volatility in this date range is 0.013452659046907695
The most recent SMA is 107.444
```

## Concepts demonstrated

- CSV parsing with `csv.DictReader`
- Return/volatility math from scratch (mean, variance, standard deviation)
- Windowed calculations (SMA) using index arithmetic
