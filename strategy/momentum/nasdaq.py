import pandas as pd
import numpy as np
import yfinance as yf

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('expand_frame_repr', False)

nasdaq = pd.read_html('https://en.wikipedia.org/wiki/Nasdaq-100')[4]
nasdaq_tickers = nasdaq.Ticker.to_list()
print(nasdaq_tickers)
print(len(nasdaq))
prices = yf.download(nasdaq_tickers, start="2009-01-01")['Adj Close']
print(prices)
prices = prices.dropna(axis=1)
print(prices)

mtl = (prices.pct_change() +1)[1:].resample('M').prod()

print(mtl)

apple = mtl.AAPL.to_list()
print(apple)

def get_rolling_ref(df, n):
    return df.rolling(n).apply(np.prod)

m12 = get_rolling_ref(mtl, 12)
m6 = get_rolling_ref(mtl, 6)
m3 = get_rolling_ref(mtl, 3)

print(m3)

top_50 = m12.loc['2022-11-30'].nlargest(50)
top_50_tickers = top_50.index

print(top_50)