import mysql.connector
from signal_engine import generate_signals

df = generate_signals()

print("Rows in signal DataFrame:", len(df))
print(df.head(5))

if df.empty:
    print("No signals to store")
    exit()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8404",
    database="stock_screener",
    auth_plugin="mysql_native_password"
)


cursor = conn.cursor()

inserted = 0

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO stock_signals
        (symbol, date, trade_signal, score, close_price)
        VALUES (%s,%s,%s,%s,%s)
    """, (
        row["symbol"],
        row["date"],
        row["trade_signal"],
        int(row["score"]),
        float(row["close_price"])
    ))
    inserted += 1

conn.commit()
conn.close()

print(f"{inserted} signals stored successfully")
