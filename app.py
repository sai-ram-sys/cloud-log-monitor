from flask import Flask
import logging
import os
import random
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

def send_email():
    try:
        msg = EmailMessage()
        msg.set_content("Error detected in cloud application log!")
        msg["Subject"] = "Cloud Alert: Error Found"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print("Email failed:", e)

@app.route('/')
def home():
    if random.randint(1,5) == 3:
        logging.error("ERROR: Something went wrong!")
        send_email()
        return "Error occurred and email sent!"
    else:
        logging.info("INFO: Normal request")
        return "App running normally."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))