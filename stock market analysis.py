import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks = [
    'HDFCBANK.NS',
    'ICICIBANK.NS',
    'SBIN.NS',
    'AXISBANK.NS',
    'KOTAKBANK.NS'
]

##downloading the stock data
data = yf.download(stocks, start="2023-01-01", end="2025-01-01")

##dropping the null values
close_prices = data['Close'].dropna()

##calculating the daily returns
daily_returns = close_prices.pct_change().dropna()

print(daily_returns.head())

##plotting the graph
daily_returns.plot(title="Daily Returns of Banking Stocks")
plt.show()

#calculating moving average
ma_20 = close_prices.rolling(window=20).mean()
ma_50 = close_prices.rolling(window=50).mean()

##plotting the graph
plt.figure(figsize=(12, 6))

plt.plot(close_prices['HDFCBANK.NS'], label='HDFC Bank Price')
plt.plot(ma_20['HDFCBANK.NS'], label='20-Day MA')
plt.plot(ma_50['HDFCBANK.NS'], label='50-Day MA')

plt.title('HDFC Bank Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

##calculating volatility 
volatility=daily_returns.std()
print(volatility)

##printing the graph
plt.figure(figsize=(10, 6))

volatility.plot(kind='bar')

plt.title('Volatility Comparison of Banking Stocks')
plt.ylabel('Volatility (Std Dev of Daily Returns)')
plt.xlabel('Stocks')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()



