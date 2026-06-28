import pandas_ta as ta
from fetch_stock_data import fetch_multiple_stocks

df = fetch_multiple_stocks()

df["SMA_20"] = ta.sma(df["Close"], length=20)
df["RSI_14"] = ta.rsi(df["Close"], length=14)
macd = ta.macd(df["Close"])
df["MACD"] = macd.iloc[:, 0]

print(df.tail())
