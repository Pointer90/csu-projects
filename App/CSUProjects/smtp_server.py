import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv

def send_form(data:dict) -> None:

    try:
        email_from = getenv('EMAIL_FROM')
        email_to = getenv('EMAIL_TO')
        token_access = getenv('EMAIL_TOKEN_ACCESS')
        smtp_server = getenv('SMTP_SERVER')
        smtp_port = getenv('SMTP_PORT')

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = 'CSU Projects'
        
        # Текст сообщения
        text_form = ""
        for elem in data:
            text_form = text_form + f'{elem}:\n\t{data[elem]}\n'
        msg.attach(MIMEText(text_form, 'plain'))

        # Подключение к сереверу и отправка
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(email_from, token_access)
        text = msg.as_string()

        server.sendmail(email_from, email_to, text)

    except Exception as e:
        print(e)
    finally:
        server.quit()