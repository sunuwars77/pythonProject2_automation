# https://myaccount.google.com/u/0/lesssecureapps?pli=1 >> To Allow
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


def send_selenium_report():
    fromaddr = 'sonamsununwar762@gmail.com'
    toaddr = "infobypokharelk@gmail.com"
    password = input("Enter password: ")
    # Email Sending Part
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Test Result"
    body = MIMEText("Hi All, <br> <br> Test for this count<br> <br> Thank You", 'html', 'utf-8')
    msg.attach(body)  # add message body (text or html)
    yourpath = 'url/TestResult.xlsx'  # path for test result or files
    for subdir, dirs, files in os.walk(yourpath):
        for filename in files:
            attachment = open(filename, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Email Sent Sucessfully")
    server.quit()
