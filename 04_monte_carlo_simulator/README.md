# Monte Carlo Portfolio Simulator

Uses the portfolio's historical statistics to simulate many possible future
outcomes, in plain Python (no pandas/numpy).

## What it does

- Reuses Project 2's `portfolio_analyzer` module (via a cross-directory
  import) to compute the weighted portfolio's historical daily return series
- Computes the historical mean and standard deviation of that return series
- Simulates 1,000 independent 30-day random paths starting from $10,000,
  drawing each day's return from `random.gauss(mean, stdev)` and compounding
- Analyzes the resulting distribution of 1,000 ending values:
  - Mean and median outcome
  - Best case / worst case
  - 5% Value-at-Risk (VaR) — the ending value below which the worst 5% of
    trials fall
  - Probability of ending below the $10,000 starting value

## How to run

```bash
cd 04_monte_carlo_simulator
python3 simulator.py
```

## Sample output

```
******Generating Report******
The simulation mean is 9554.980867495062
The simulation median is 9549.688554816254
The best case is 11083.454998872296 and the worst case is 8093.595673328516
There is a 5% chance you will fall under this value: 8853.420572606874
The fraction of trials that fall under the starting value of 10000 is 0.842
```

## Concepts demonstrated

- Cross-directory module reuse (`sys.path.append` with a path built from
  `os.path.dirname(os.path.abspath(__file__))`, so the import works
  regardless of the caller's working directory)
- Monte Carlo simulation via repeated random sampling and compounding
- Distribution analysis without a stats library: median and percentile
  (VaR) computed by sorting and indexing directly into the sorted list
