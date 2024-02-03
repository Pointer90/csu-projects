from django.shortcuts import render
from .models import Projects, Workers, Subprojects, Vacancies, WorkersInSubprojects
from .smtp_server import send_form

# Create your views here.

def main(request):
    data = Projects.objects.exclude(status='completed').exclude(status='frozen')
    workers_count = Workers.objects.count()
    projects_count = Projects.objects.count()
    completed_projects_count = Projects.objects.filter(status='completed').count()

    # Отправка почты
    if request.method == "POST":
        data = dict()
        form_names = ['title_project', 'title_organization', 'email', 'vacancy', 'description']

        for name in form_names:
            data[name] = request.POST.get(name)
            send_form(data)

    return render(request, 'index.html', context={"cards": data,
                                                  "wcount" : workers_count,
                                                  "pcount": projects_count,
                                                  "cpcount": completed_projects_count})

def subProjects(request, pid):
    name = Projects.objects.get(pid=pid)
    data = Subprojects.objects.filter(pid=pid)
    vacs = Vacancies.objects.select_related('sid').filter(sid__pid=pid).values("vid", "post", "description")

    # Отправка почты
    if request.method == "POST":
        data = dict()
        form_names = ['name', 'second_name', 'group', 'email', 'subporject_name', 'vacancy', 'description']

        for name in form_names:
            data[name] = request.POST.get(name)
            send_form(data)

        

    return render(request, 'subProjects.html', context= {"project" : name, "cards" : data, "vacancies": vacs})

def completedProjects(request):
    data = Subprojects.objects.select_related('pid').filter(status='completed').values('pid', 'pid__title', 'pid__description').distinct()
    return render(request, 'completedProjects.html', context= {"cards": data})

def cinema(request, pid):
    name = Projects.objects.get(pid=pid)
    data = WorkersInSubprojects.objects.select_related('sid', 'wid').filter(sid__pid=pid)
    return render(request, 'cinema.html',context= {'project': name, 'cards': data})