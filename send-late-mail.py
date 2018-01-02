#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from random import choice
from sys import argv

script, time = argv

MSG = [
        'As I woke up late, today I came {0} minutes lately to the office.',
        'As I got struck in railway track, toady I came {0} minutes lately to the office.',
        'As I got struck in traffic, today I came {0} minutes lately to the office.',
        ]
SENDER = 'karthik@sodexis.com'
RECIVER = 'v.s.elangovan@sodexis.com'
pwd = 'Karthik1@'

# frame msg
msg = MIMEMultipart()
msg['From'] = SENDER
msg['To'] = RECIVER
msg['Subject'] = 'Reg - Came Late'
message = choice(MSG).format(time)
main_message = """
Dear Sir,
{0} Please accept my request.
\n--
Karthik Arumugam
Sodexis Team
www.sodexis.com
issues@sodexis.com""".format(message)
print main_message
msg.attach(MIMEText(main_message))

mail_server = smtplib.SMTP_SSL('smtp.gmail.com',465)

mail_server.ehlo()

mail_server.login(SENDER, pwd)

mail_server.ehlo()

try:
    mail_server.sendmail(SENDER, RECIVER, msg.as_string())
finally:
    mail_server.quit()
