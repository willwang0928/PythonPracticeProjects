# CSV Stock Data Analyzer (plain Python -- no pandas/numpy)
# Reads daily stock price data from data.csv and prints a summary report:
# date range, average daily return, volatility, and most recent SMA.

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
    mean = sum(dr) / len(dr)
    
    deviation = []
    for val in dr:
        deviation.append(math.pow(val-mean, 2))
    
    variance = sum(deviation) / len(deviation)
        
    sd = math.sqrt(variance)
    
    return sd
    

if __name__ == "__main__":
    main()
