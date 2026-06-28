import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="8404",
    database="stock_screener",
    auth_plugin="mysql_native_password"
)

query = """
SELECT s.symbol,
       s.trade_signal,
       s.score,
       s.date
FROM stock_signals s
JOIN (
    SELECT symbol, MAX(created_at) AS latest_time
    FROM stock_signals
    GROUP BY symbol
) latest
ON s.symbol = latest.symbol
AND s.created_at = latest.latest_time
ORDER BY s.score DESC;
"""

df = pd.read_sql(query, conn)
conn.close()

print("\n=== 📊 TRADINGVIEW-STYLE SCREENER OUTPUT ===\n")
print(df.to_string(index=False))
