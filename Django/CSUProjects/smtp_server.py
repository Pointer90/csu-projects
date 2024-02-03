import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ

def send_form(data:dict) -> None:

    try:

        # Формирую шапку письма
        # email_from = environ.get("EMAIL_FROM")
        # email_to = environ.get("EMAIL_TO")
        # token_access = environ.get("EMAIL_TOKEN_ACCESS")
        # smtp_server = environ.get("SMTP_SERVER")
        # smtp_port = environ.get("SMTP_PORT")

        # Todo: Убрать шаблоны
        email_from = "user1@example.com"
        email_to = "user1@example.com"
        token_access = "rs1fz1knh1wc1xoy"
        smtp_server = "smtp.example.ru"
        smtp_port = 465

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

        # Отправка письма на почту себе и получателю
        server.sendmail(email_from, email_to, text)

    except Exception as e:
        # Todo: Добавить обработчик
        print(e)
    finally:
        server.quit()