# Multi-Stock Portfolio Analyzer (plain Python -- no pandas/numpy)
# Loads daily price data for multiple tickers and computes weighted
# portfolio returns/volatility, plus pairwise correlation between tickers.

import csv
import math

def main():
    all_tickers = load_all(['AAPL', 'GOOG', 'MSFT'])
    weight = {'AAPL': 0.5, 'MSFT': 0.3, 'GOOG': 0.2}
    print("***********Generating report***********")
    
    print(f'Tickers included: {list(weight.keys())}')
    print(f'Weight of each stock in portfolio: {weight}')

    all_returns = all_daily_returns(all_tickers)
    port_r = portfolio_return(all_returns, weight)
    aver_portfolio = sum(port_r) / len(port_r)
    print(f'The average portfolio daily return is {aver_portfolio}.')

    print(f'The portfolio volatility is {portfolio_vol(port_r)}.')

    print('Correlation matrix:')
    for t1, t2, c in all_correlation(all_returns):
        print(f'  {t1}-{t2}: {c}')

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
    
def daily_returns(ticker): # row of dicts for one ticker
    l = []
    for i in range(len(ticker)):
        if i != 0:
            l.append(((float(ticker[i]['close']) - float(ticker[i-1]['close'])) / float((ticker[i-1]['close']))))

    return l

def all_daily_returns(tickers):
    l = {}
    for ticker in tickers:
        l[ticker] = daily_returns(tickers[ticker])
        
    return l

def portfolio_return(r, weight):
    num_days = len(r['AAPL'])
    returns = []
    for i in range(num_days):
        day_total = 0
        for t in r:
            day_total = day_total + r[t][i] * weight[t]
        returns.append(day_total)
    return returns
        
def portfolio_vol(portfolio):
    mean = sum(portfolio) / len(portfolio)
    
    deviation = []
    for val in portfolio:
        deviation.append(math.pow(val-mean, 2))
    
    variance = sum(deviation) / len(deviation)
        
    sd = math.sqrt(variance)
    
    return sd

def covariance(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    
    tot = 0
    for i in range(len(x)):
        tot = tot + (x[i] - mean_x) * (y[i] - mean_y)
        
    return tot / len(x)

def correlation(x,y):
    return covariance(x, y) / (portfolio_vol(x) * portfolio_vol(y))
def all_correlation(portfolio):
    tl = list(portfolio.keys())
    corr = []
    for i in range(len(portfolio)):
        for j in range(i+1, len(portfolio)):
            corr.append((tl[i], tl[j], correlation(portfolio[tl[i]], portfolio[tl[j]])))
    return corr
    
if __name__ == "__main__":
    main()