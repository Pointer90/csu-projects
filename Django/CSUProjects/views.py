from django.shortcuts import render, HttpResponse
from .models import Projects, Workers, Subprojects, Vacancies, WorkersInSubprojects

# Create your views here.

def main(request):
    data = Projects.objects.exclude(status='completed').exclude(status='frozen')
    workers_count = Workers.objects.count()
    projects_count = Projects.objects.count()
    completed_projects_count = Projects.objects.filter(status='completed').count()
    return render(request, 'index.html', context={"cards": data,
                                                  "wcount" : workers_count,
                                                  "pcount": projects_count,
                                                  "cpcount": completed_projects_count})

def subProjects(request, pid):
    data = Subprojects.objects.filter(pid=pid)
    name = Projects.objects.get(pid=pid)
    return render(request, 'subProjects.html', context= {"project" : name, "cards" : data})

def completedProjects(request):
    data = Subprojects.objects.select_related('pid').filter(status='completed').values('pid', 'pid__title', 'pid__description').distinct()
    return render(request, 'completedProjects.html', context= {"cards": data})

def cinema(request, pid):
    name = Projects.objects.get(pid=pid)
    data = WorkersInSubprojects.objects.select_related('sid', 'wid').filter(sid__pid=pid)
    return render(request, 'cinema.html',context= {'project': name, 'cards': data})