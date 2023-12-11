from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def main(request):
    data = Projects.objects.all()
    return render(request, 'index.html', context={"cards": data})

def subProjects(request, prj_id):
    data = SubProjects.objects.filter(prj_id=prj_id)
    return render(request, 'subProjects.html', context= {"cards" : data})

def completedProjects(request):
    data = Projects.objects.all()
    return render(request, 'completedProjects.html', context= {"cards": data})

def cinema(request, prj_id):
    name = Projects.objects.get(prj_id=prj_id)
    data = WorkersInProject.objects.select_related('worker_id').filter(prj_id=prj_id)
    size = 1000
    for d in data:
        size += 1500
    print(size)
    #! TODO решить проблему динамического изменения размера страницы
    return render(request, 'cinema.html',context= {'nameProject': name, 'cards': data, 'size': size})