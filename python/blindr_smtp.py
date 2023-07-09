import smtplib
from email.mime.text import MIMEText

subject = "SMTP Test"
body = "This is a test e-mail message."
sender = "sender@gmail.com"
recipients = ["recipient@domain.com"]
password = input("Type your password and press enter: ")


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)