import smtplib
import csv
import os
from email.message import EmailMessage
from datetime import datetime

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_ID = "mohammedzubairuddinzameer@gmail.com"
APP_PASSWORD = "snbc pmeh bfxy lakz"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


csv_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".csv")]

if not csv_files:
    raise FileNotFoundError("No CSV file found in script directory")

CSV_FILE = os.path.join(BASE_DIR, csv_files[0])
print("Using CSV file:", CSV_FILE)

def send_bulk_emails(csv_path):
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login(EMAIL_ID, APP_PASSWORD)

    with open(csv_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        print("Detected CSV headers:", reader.fieldnames)

        for row in reader:
            email = row.get("email") or row.get("Email")
            name = row.get("name") or row.get("Name") or "User"

            if not email:
                continue

            msg = EmailMessage()
            msg["From"] = EMAIL_ID
            msg["To"] = email
            msg["Subject"] = "Hackveda – Python Email Automation"

            msg.set_content(f"""
Hello {name},

We analyzed your website and found it relevant for digital collaboration.

This is an automated email sent using Python
for Hackveda Business Operations.

Sent at: {datetime.now().strftime('%Y-%m-%d \t \t  %H:%M:%S')}

Regards,
Mohammed Zubair Uddin Zameer
""")

            server.send_message(msg)
            print(f"✔ Email sent to {name} ({email})")

    server.quit()
    print("✔ Bulk email process completed.")



send_bulk_emails(CSV_FILE)
