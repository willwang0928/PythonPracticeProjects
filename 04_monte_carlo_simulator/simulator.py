# Monte Carlo Portfolio Simulator (plain Python -- no pandas/numpy)
# Uses the portfolio's historical mean/volatility (from Project 2) to run
# 1000+ randomized future price paths and reports the outcome distribution:
# mean, median, best/worst case, 5% VaR, and probability of loss.
import sys
import os
import math
import random
this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(this_dir, '..', '02_portfolio_analyzer'))
import portfolio_analyzer as pa
# Build the path to Project 2's folder relative to THIS file's location on
# disk (not relative to whatever directory you happen to run the script
# from) -- this makes the import work no matter where you run it from.
def main():
    returns = port_returns()
    mean, sd = portfolio_stats(returns)
    start_value = 10000
    sims = run_simulations(start_value, mean, sd, 30, 1000)
    
    best = max(sims)
    worst = min(sims)
    mean_sims = sum(sims) / len(sims)
    
    sorted_sims = sorted(sims)
    
    median = 0
    if len(sims) % 2 == 0:
        median = (sorted_sims[len(sims)//2 - 1] + sorted_sims[len(sims)//2]) / 2
    else:
        median = sorted_sims[(len(sims) - 1) // 2]
    
    index = int(0.05 * len(sorted_sims))
    VaR = sorted_sims[index]
    count = 0
    for val in sorted_sims:
        if val < start_value:
            count += 1
        else:
            break
    prob_loss = count / len(sims)
    
    print('******Generating Report******')
    print(f'The simulation mean is {mean_sims}')
    print(f'The simulation median is {median}')
    print(f'The best case is {best} and the worst case is {worst}')
    print(f'There is a 5% chance you will fall under this value: {VaR}')
    print(f'The fraction of trials that fall under the starting value of {start_value} is {prob_loss}')
        

def port_returns():
    tickers = pa.load_all(['AAPL', 'GOOG', 'MSFT'])
    all_returns = pa.all_daily_returns(tickers)
    weights = {'AAPL': 0.5, 'MSFT': 0.3, 'GOOG': 0.2}

    port_return = pa.portfolio_return(all_returns, weights)
    return port_return

def portfolio_stats(p_returns):
    mean = sum(p_returns) / len(p_returns)
    
    deviation = []
    for val in p_returns:
        deviation.append(math.pow(val-mean, 2))
    
    variance = sum(deviation) / len(deviation)
    stdev = math.sqrt(variance)
    
    return mean, stdev

def simulate_path(start_value, mean, stdev, num_days):
    compounding = start_value
    
    for i in range(num_days):
        compounding = (random.gauss(mean, stdev) + 1) * compounding
        
    return compounding

def run_simulations(start_value, mean, stdev, num_days, num_trials):
    sims = [simulate_path(start_value, mean, stdev, num_days) for i in range(num_trials)]    
    
    return sims

if __name__ == "__main__":
    main()