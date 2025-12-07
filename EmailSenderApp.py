import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Your Name"
email["to"] = "receiver@example.com"
email["subject"] = "Test Email from Python"

email.set_content("Hello! This is an automatic email using Python.")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.starttls()
    smtp.login("your_email@gmail.com", "your_app_password")
    smtp.send_message(email)
    print("Email sent!")
