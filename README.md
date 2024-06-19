# CSU | Projects
![Static Badge](https://img.shields.io/badge/Python-3.11-green) ![Static Badge](https://img.shields.io/badge/Django-4.2.6-yellow) ![Static Badge](https://img.shields.io/badge/Gunicorn-21.2.0-yellow) ![Static Badge](https://img.shields.io/badge/Docker-24.0.6-blue) ![Static Badge](https://img.shields.io/badge/Nginx-1.25-blue) ![Static Badge](https://img.shields.io/badge/Bootstrap-5-purple)

Клиент-серверное приложение для университета ЧелГУ

> Сайт "визитка" содержащий подробное описание всех проектов университета ЧелГУ. Благодаря сайту можно посмотреть, какие проекты уже выполнены, кто над ними работал, а также проекты находящиеся в разработке.
Стек технологий: Bootstap + Django + Python + SQLite

### Первое развертывание приложения.

Скачивание образов (Django выдаст ошибку — игнорируем).
```powershell
docker compose -f ./docker-compose.prod.yml build
```
Запускаем отдельно контейнер "db" в CLI пишем
```powershell
psql -U postgres;
psql create user <POSTGRES_USER> with PASSWORD <POSTGRES_PASSWORD>;
psql create database <POSTGRES_NAME>;
\q
```
Для запуска контейнеров используем
```powershell
docker compose -f ./docker-compose.prod.yml up
```
