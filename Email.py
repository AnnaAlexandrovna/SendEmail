#! /usr/bin/env python3
# def send_mail(listOfRecipients, listOfName):



import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "salatik3392@yandex.ru"
listOfRecipients = ['anna.karakhanova@yandex.ru', "salatik339@mail.ru"]
listOfName = ['anna', 'salatik']

for listOfRecipients, listOfName in zip(listOfRecipients, listOfName):
    msg = MIMEMultipart('multipart')
    msg['Subject'] = "Hi, " + listOfName
    msg['From'] = me
    msg['To'] = listOfRecipients

    #text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
            <html>
              <head></head>
              <body>
                <p>Hi, %s!<br>
                </p>
              </body>
            </html>
            """ %(listOfName)

    #part1 = MIMEText(text, 'plain', 'utf-8')
    part2 = MIMEText(html, 'html', 'utf-8')

    #msg.attach(part1)
    msg.attach(part2)

    try:
        s = smtplib.SMTP('smtp.yandex.ru')
        s.ehlo()
        s.starttls()
        s.login('salatik3392@yandex.ru', 'Atos2018*')
        s.sendmail(me, listOfRecipients, msg.as_string())
        s.quit()
    except Exception as e:
        print(f'Oh no! Something bad happened!\n {e}')
