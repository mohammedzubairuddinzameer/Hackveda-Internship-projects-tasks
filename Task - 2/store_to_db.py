import mysql.connector
from indicators import df

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8404",
    database="stock_screener",
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO stocks
    (symbol, date, close_price, volume, sma_20, rsi_14, macd)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
""", (
    row["symbol"],
    row["Date"],
    float(row["Close"]),
    int(row["Volume"]),
    row["SMA_20"] if row["SMA_20"] == row["SMA_20"] else None,
    row["RSI_14"] if row["RSI_14"] == row["RSI_14"] else None,
    row["MACD"] if row["MACD"] == row["MACD"] else None
))


conn.commit()
conn.close()

print("Data stored in MySQL successfully")
