import time
import smtplib
from email.message import EmailMessage

EMAIL = "sairamnair.18@gmail.com"
PASSWORD = "orslkhzrhjliaxnn"

def send_email():
    try:
        msg = EmailMessage()
        msg.set_content("Error detected in cloud application log!")
        msg["Subject"] = "Cloud Alert: Error Found"
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        print("Connecting to Gmail...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD)
            print("Login successful!")
            server.send_message(msg)
            print("Email sent successfully!")

    except Exception as e:
        print("Email failed:", e)

while True:
    print("Checking log...")
    with open("app.log", "r") as file:
        logs = file.read()
        if "ERROR" in logs:
            print("ERROR detected!")
            send_email()
            break
    time.sleep(5)