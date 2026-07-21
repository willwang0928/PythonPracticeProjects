# CAPM / Factor Regression + Risk Report (plain Python -- no pandas/numpy)
# Portfolio class wrapping volatility, Sharpe, and max drawdown as methods,
# plus manual least-squares regression for each stock's beta/alpha vs. SPY.
import sys
import os
import math

this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(this_dir, '..', '02_portfolio_analyzer'))
import portfolio_analyzer as pa

class Portfolio:
    def __init__(self, tickers, weights):
        self.tickers = tickers
        self.weights = weights
        
        ticks = pa.load_all(self.tickers)
        self.returns = pa.all_daily_returns(ticks)
        self.port_returns = pa.portfolio_return(self.returns, self.weights)
        
        spy = pa.load_ticker('SPY.csv')
        self.benchmark_returns = pa.daily_returns(spy)
    def volatility(self):
        mean = sum(self.port_returns) / len(self.port_returns)
        
        deviation = []
        for val in self.port_returns:
            deviation.append(math.pow(val-mean, 2))
            
        variance = sum(deviation) / len(deviation)
        
        sd = math.sqrt(variance)
        
        return sd
    
    def sharpe(self):
        mean = sum(self.port_returns) / len(self.port_returns)
        
        deviation = []
        for val in self.port_returns:
            deviation.append(math.pow(val-mean, 2))
            
        variance = sum(deviation) / len(deviation)
        
        sd = math.sqrt(variance)
        
        sharpe = mean / sd
        annul_sharpe = sharpe * math.sqrt(252)
        return sharpe, annul_sharpe
    
    def max_drawdown(self):
        start_val = 10000
        equity = []
        for val in self.port_returns:
            start_val = start_val*(1 + val)
            equity.append(start_val)
        
        h = 0
        drawdown = []
        for val in equity:
            if val > h:
                h = val
            drawdown.append((h - val) / h)
            
        return max(drawdown)
    
    def beta_alpha(self, ticker):
        x = self.benchmark_returns # benchmark returns
        y = self.returns[ticker] # given ticker returns
        
        mean_y = sum(y) / len(y)
        mean_x = sum(x) / len(x)
            
        variance = pa.covariance(x, x)
        beta = pa.covariance(x, y) / variance
        alpha = mean_y - beta * mean_x
        
        return beta, alpha
    
def main():
    tickers = ['AAPL', 'MSFT', 'GOOG']
    weights = {'AAPL': 0.5, 'MSFT': 0.3, 'GOOG': 0.2}
    portfolio = Portfolio(tickers, weights)
    print(f"The portfolio's volatility is {portfolio.volatility()}")
    print(f"The portfolio's Sharpe ratio is {portfolio.sharpe()}")
    print(f"The portfolio's max drawdown is {portfolio.max_drawdown()}")
    for ticker in tickers:
        print(f"{ticker}'s beta/alpha is {portfolio.beta_alpha(ticker)}")
    
if __name__ == "__main__":
    main()
        
            
        
        