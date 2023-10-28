from django.shortcuts import render, HttpResponse

# Create your views here.

# TODO: Убрать пример поступаемых данных
data = {
    'cards': [
        {'name': 'Методы ИИ в образовательной траектории школьника',
         'url': '/subProjects',
          'content': 'Создание цифровых продуктов для автоматизации дополнительного образования школьника. Площадка реализации ОЦ №5'},
        {'name': 'Проекты ЧелГУ',
         'url': '#',
          'content': 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты.'},
    ]
}

def main(request):
    return render(request, 'index.html', context= data)

def subProjects(request):
    return render(request, 'subProjects.html')