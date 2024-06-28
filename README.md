# CSU | Projects
![Static Badge](https://img.shields.io/badge/Python-3.11-green) ![Static Badge](https://img.shields.io/badge/Django-4.2.6-yellow) ![Static Badge](https://img.shields.io/badge/Gunicorn-21.2.0-yellow) ![Static Badge](https://img.shields.io/badge/Docker-24.0.6-blue) ![Static Badge](https://img.shields.io/badge/Nginx-1.25-blue) ![Static Badge](https://img.shields.io/badge/Bootstrap-5-purple)

### Клиент-серверное приложение для университета ЧелГУ

> Сайт "визитка" содержащий подробное описание всех проектов университета ЧелГУ. Благодаря сайту можно посмотреть, какие проекты уже выполнены, кто над ними работал, а также проекты находящиеся в разработке.
Стек технологий: Bootstap + Django + Python + PostgreSQL

### Развертывание приложения.
Для корректной работы приложения необходимо заполнить файл с переменными окружения (для удобства в корне проекта существует шаблон .env_template). Рекомендуется назвать файл ".env".
Далее в CLI следует выполнить команду:
```powershell
docker compose -f ./docker-compose.prod.yml up
```
Если приложение развертывается первый раз и базы данных ещё не существует, то запускаем отдельно контейнер "web" и в CLI пишем:
```powershell
python manage.py createsuperuser
```
Для запуска контейнеров используем:
```powershell
docker compose -f ./docker-compose.prod.yml up
```
