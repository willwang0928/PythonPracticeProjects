# Moving-Average Crossover Backtester (plain Python -- no pandas/numpy)
# Simulates a fast/slow SMA crossover strategy on AAPL.csv and reports
# total return, Sharpe ratio, and max drawdown vs. a buy-and-hold baseline.

import csv
import math
def main():
    closes, dates = load('AAPL.csv')
    fast = sma(closes, 5)
    slow = sma(closes, 20)
    positions = generate_signals(fast, slow)
    returns, acc, count = simulate(closes, positions)
    
    print('******Generating report******')
    print(f'Total return: {(acc[-1] - 10000) / 10000}')
    print(f'This is how many times your strategy traded: {count}')
    print(f'Buy-and-hold total return: {(closes[-1] - closes[0]) / closes[0]}')
    print(f'The daily and annual Sharpe ratios are {daily_sharpe(returns)} (daily) and {annual_sharpe(daily_sharpe(returns))} (annual)')
    print(f'The max drawdown is {max_drawdown(acc)}')
    
def load(filename):
    close = []
    date = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            close.append(float(row['close']))
            date.append(row['date'])
            
    return close, date

def sma(closes, window):
    l = []
    for c in range(len(closes)):
        if c - window + 1 >= 0:
            mean = 0
            for j in range(c - window + 1, c + 1):
                mean += closes[j]
            mean = mean / window
            l.append(mean)
    return l

def generate_signals(fast_sma, slow_sma):
    diff = len(fast_sma) - len(slow_sma)
    fast_sma = fast_sma[diff:]
    signal = []
    for i in range(len(fast_sma)):
        strat = 0
        if fast_sma[i] > slow_sma[i]:
            strat = 1
        signal.append(strat)
    return signal

def simulate(closes, positions):
    daily_ret = []
    count = 0
    acc = []
    value = 10000
    diff = len(closes) - len(positions)
    closes = closes[diff:]
    for i in range(len(closes)):
        if positions[i] == 1 and i != 0:
            daily_ret.append((closes[i] - closes[i-1]) / closes[i-1])
            value = ((closes[i] - closes[i-1]) / closes [i-1] + 1) * value
            acc.append(value)
        elif i != 0:
            daily_ret.append(0)
            acc.append(value)
            
    for i in range(len(positions)):
        if i != 0 and positions[i] != positions[i-1]:
            count += 1
            
    
    return daily_ret, acc, count

def daily_sharpe(daily_ret):
    mean = sum(daily_ret) / len(daily_ret)
    deviation = []
    
    for val in daily_ret:
        deviation.append(math.pow(val-mean, 2))
        
    variance = sum(deviation) / len(deviation)
    
    sd = math.sqrt(variance)
    
    return mean / sd

def annual_sharpe(daily):
    return daily * math.sqrt(252)

def max_drawdown(acc):
    h = 0
    drawdown = []
    for val in acc:
        if val > h:
            h = val
        drawdown.append((h - val) / h)
    
    max_draw = 0
    for val in drawdown:
        if val > max_draw:
            max_draw = val
    
    return max_draw
    


if __name__ == "__main__":
    main()
    

