from flask import Flask
import logging
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

print("===== APP STARTED =====")
print("EMAIL loaded:", EMAIL is not None)
print("PASSWORD loaded:", PASSWORD is not None)

def send_email():
    print(">>> send_email() function triggered")

    if not EMAIL or not PASSWORD:
        print("❌ Environment variables NOT loaded!")
        return

    try:
        msg = EmailMessage()
        msg.set_content("Error detected in cloud application!")
        msg["Subject"] = "Cloud Alert: Error Found"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        print("Connecting to Gmail SMTP...")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            print("Logging in...")
            server.login(EMAIL, PASSWORD)
            print("✅ Login successful!")

            server.send_message(msg)
            print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Email failed:", e)


@app.route('/')
def home():
    print(">>> '/' route triggered")

    logging.error("ERROR: Something went wrong!")

    send_email()

    return "Error occurred and email process attempted!"
