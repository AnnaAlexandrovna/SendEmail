#! /usr/bin/env python3
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "salatik3392@yandex.ru"
listOfRecipients = ['anna.karakhanova@yandex.ru', "salatik339@mail.ru"]

msg = MIMEMultipart('multipart')
msg['Subject'] = "Test"
msg['From'] = me
msg['To'] = ', '.join(listOfRecipients)

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, 'plain', 'utf-8')
part2 = MIMEText(html, 'html', 'utf-8')

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('smtp.yandex.ru')
s.ehlo()
s.starttls()
s.login('salatik3392@yandex.ru', 'Atos2018*')
s.sendmail(me, listOfRecipients, msg.as_string())
s.quit()