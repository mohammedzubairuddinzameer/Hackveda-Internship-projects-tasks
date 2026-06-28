import yfinance as yf
import pandas as pd

SYMBOLS = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]

def fetch_multiple_stocks():
    all_data = []

    for symbol in SYMBOLS:
        df = yf.download(symbol, period="6mo", interval="1d")

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.reset_index(inplace=True)
        df["symbol"] = symbol
        all_data.append(df)

    return pd.concat(all_data, ignore_index=True)

