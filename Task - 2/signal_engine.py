import mysql.connector
import pandas as pd

def generate_signals():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8404",
        database="stock_screener",
        auth_plugin="mysql_native_password"
    )

    query = """
    SELECT symbol, date, close_price, sma_20, rsi_14, macd
    FROM stocks
    WHERE rsi_14 > 0
    ORDER BY date DESC
    """

    df = pd.read_sql(query, conn)
    conn.close()

    def compute(row):
        score = 0

        if row["rsi_14"] < 30:
            score += 30
        elif row["rsi_14"] < 60:
            score += 15
        else:
            score += 5

        if row["close_price"] > row["sma_20"]:
            score += 25

        if row["macd"] and row["macd"] > 0:
            score += 25

        if score >= 70:
            signal = "BUY"
            icon = "🟢"
        elif score >= 45:
            signal = "HOLD"
            icon = "🟡"
        else:
            signal = "SELL"
            icon = "🔴"

        return f"{icon} {signal}", score

    df[["trade_signal", "score"]] = df.apply(
        lambda r: pd.Series(compute(r)), axis=1
    )

    
    summary = (
        df.groupby("trade_signal")["symbol"]
        .unique()
        .apply(lambda x: ", ".join(x))
    )

    print("\n📊 Signals created →", " | ".join(
        [f"{k}: {v}" for k, v in summary.items()]
    ))

    return df
if __name__ == "__main__":
    df = generate_signals()
