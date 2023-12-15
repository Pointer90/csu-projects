From python:3.11

SHELL [ "/bin/bash", "-c"]

WORKDIR /app
COPY . .

RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "./Django/manage.py", "makemigrations" ]
CMD ["python", "./Django/manage.py", "migrate"]