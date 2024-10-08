FROM python:3.11-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG HTTP_PROXY

RUN pip install --proxy $HTTP_PROXY --upgrade pip
COPY requirements.txt .
RUN pip install --proxy $HTTP_PROXY -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn Config.wsgi:application --bind 0.0.0.0:8000"]