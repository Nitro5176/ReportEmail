import smtplib
import ssl
import time
import getpass
import Stocks

port = 465  # for SSL
smtp_server = "smtp.gmail.com"
sender_email = "@gmail.com"  # Enter your address
receiver_email = "@gmail.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
password = getpass.getpass("Password: ")
message = """\
Subject: Hi there

Stocks"""

context = ssl.create_default_context()  # create a secure SSL  context

message = message + Stocks.amc_stocks() + Stocks.amd_stocks()

while True:

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    time.sleep(60)
