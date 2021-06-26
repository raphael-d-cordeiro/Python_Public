# script for replace placeholders
from string import Template
from datetime import datetime

from data_email import my_email, my_password
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    date_now = datetime.now().strftime('%d/%m/%Y')
    body_msg = template.safe_substitute(nome='NAME USER FOR PLACEHOLDER', data=date_now)

msg = MIMEMultipart()
msg['from'] = 'YOUR NAME HERE'
msg['to'] = 'emaildestination@domain.com'
msg['subject'] = 'SUBJECT EMAIL'

body_msg = MIMEText(body_msg, 'html')
msg.attach(body_msg)

with open('default.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(my_email, my_password)
    smtp.send_message(msg)
    print('E-mail sent succesfuly!')