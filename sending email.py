import smtplib
import os
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

html = Template(Path("index.html").read_text())
msg = EmailMessage()
me = "Melinda T."
receiver = os.getenv("EMAIL_RECEIVER")
msg["from"] = me
msg["to"] = receiver
msg["subject"] = "You will never believe it !!!"
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

msg.set_content(html.substitute({"name": "Mel"}), "html")


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp_server:
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email_address, email_password)
    smtp_server.send_message(msg)
    print("Send")
