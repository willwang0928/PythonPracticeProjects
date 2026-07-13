# Project 1: CSV Stock Data Analyzer (Plain Python — no pandas/numpy)
#
# Goal: read a CSV of daily stock price data and print a summary report.
# Use only core Python: the `csv` module, loops, lists/dicts, functions.
#
# The CSV (data.csv, in this same folder) has columns:
#   date, open, high, low, close, volume
#
# What your script should do:
#
# 1. Read data.csv and load it into a data structure of your choice
#    (e.g. a list of dicts, one per row).
#
# 2. Compute the daily return for each day, where:
#    daily_return = (close_today - close_yesterday) / close_yesterday
#    (there's no return for the first day, since there's no prior close)
#
# 3. Compute a simple moving average (SMA) of the closing price over a
#    window of N days (pick N, e.g. 5). For each day where you have at
#    least N prior closes, the SMA is the average close over that window.
#
# 4. Compute volatility: the standard deviation of the daily returns
#    you calculated in step 2. (Standard deviation = sqrt of the average
#    squared deviation from the mean. No numpy — write this yourself.)
#
# 5. Print a summary report to the console with:
#    - the date range covered by the data
#    - the average daily return
#    - the volatility (std dev of daily returns)
#    - the most recent SMA value
#
# Notes:
# - Write this as functions (e.g. load_data, compute_returns,
#   compute_sma, compute_volatility) rather than one long script.
# - Think about what each function takes in and returns before writing it.
# - Ping for help if you get stuck on something specific — not for the
#   full answer, just to talk through the blocker.
import csv
import math

def main():    
    with open('data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        c, d = get_close_date(reader)
        returns = daily_returns(c)
        sma = SMA(c)
        
        print("***********Generating report***********")
        print(f"Date range: {d[0]} - {d[-1]}")
        print(f"The average daily return is {sum(returns)/len(returns)}")
        print(f"The volatility in this date range is {volatility(returns)}")
        print(f"The most recent SMA is {sma[-1]}")
        
        
def get_close_date(reader):
    close = []
    date = []
    for row in reader:
        close.append(float(row['close']))
        date.append(row['date'])
    return close, date

    
def daily_returns(close):
    returns = []
    for i in range(len(close)):
        if i != 0:
            returns.append((close[i]-close[i-1])/close[i-1])
            
    return returns
    
def SMA(close):
    sma = []
    for i in range(len(close)):
        if i > 3:
            sma.append((close[i]+close[i-1]+close[i-2]+close[i-3]+close[i-4])/5)
    return sma

def volatility(dr):
    mean = 0
    for value in dr:
        mean = mean + value
    mean = mean/len(dr)
    
    deviation = []
    for val in dr:
        deviation.append(math.pow((val-mean), 2))
    
    variance = 0
    for v in deviation:
        variance = variance + v
    sd = math.sqrt(variance/len(deviation))
    
    return sd

    
    

if __name__ == "__main__":
    main()
