from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

# TODO: Убрать пример поступаемых данных когда сделаем бд
dataMainPage = {
    'cards': [
        {'name': 'Методы ИИ в образовательной траектории школьника',
         'url': '/subProjects',
          'content': 'Создание цифровых продуктов для автоматизации дополнительного образования школьника. Площадка реализации ОЦ №5'},
        {'name': 'Проекты ЧелГУ',
         'url': '#',
          'content': 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.'},
    ]
}

dataSubPage = {
    'cards': [
        {'name': 'Личный кабинет учителя. Автономная программа',
         'url': '#',
         'content': 'Создание базы данных заданий по разным школьным предметам. Техническое сопровождение выстраивания индивидуальной траектории обучения. Ведение внеучебной документации.'},
        {'name': 'Личный кабинет школьника. Web-приложение',
         'url': '#',
         'content': 'Создание приложения в функционал которого входит возможность выполнять индивидуальные задания, участвовать в рейтинге, общение с психологом.'},
        {'name': 'Применение ИИ при обработке изображений',
         'url': '#',
         'content': 'Задача методами ИИ установить взаимосвязь между возрастом, успеваемостью и психологическим портретом школьника.'},
    ]
}

dataCompletedPage = {
    'cards': [
        {'name': 'Мобильное приложение расписание ЧелГУ',
         'url': '#',
         'content': 'Приложение для быстрого доступа и мониторинга расписания ЧелГУ'}
    ]
}

dataCinemaPage = {
    'nameProject': 'Мобильное приложение расписание ЧелГУ',
    'cards': [
        {'name': 'Карпенко Дмитрий',
         'post': 'Разработчик',
         'content': 'Разработка базы данных, клиентской части с использованием Flutter.',
         'side': 1 # 1 - Слева, 0 - Справа
        },
        {'name': 'Шарманова Оксана',
         'post': 'Разработка дизайна',
         'content': 'Разработка дизайна, клиентской части проекта.',
         'side': 0
        },
        {'name': 'Плеханова Марина Васильевна',
         'post': 'Руководитель проекта',
         'content': 'Ведение жизненного цикла разработки приложения - от идеи до выпуска.',
         'side': 1
        },
    ]
}

def main(request):
    projects = Projects.objects.all()
    return render(request, 'index.html', context={"projects": projects})

def subProjects(request):
    return render(request, 'subProjects.html', context= dataSubPage)

def completedProjects(request):
    return render(request, 'completedProjects.html', context= dataCompletedPage)

def cinema(request):
    data = Workers.objects.all()
    return render(request, 'cinema.html',context= {'workers': data})