from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Projects, Workers, Subprojects, Vacancies, WorkersInSubprojects
from .smtp_server import send_form

# Create your views here.

def set_cookie(response, **kwargs):
    for key, value in kwargs.items():
        response.set_cookie(key, value)
    
    return response

def format_phone(prj: Projects) -> str:
    return f'{prj.phone[0]}({prj.phone[1:4]})-{prj.phone[4:7]}-{prj.phone[7:9]}-{prj.phone[9:]}'


def main(request):
    data = Projects.objects.exclude(status='completed').exclude(status='frozen')
    data_paginator = Paginator(data, 10)

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

    page_number = request.GET.get("page")
    needed_page = data_paginator.get_page(page_number)
    context = {"template_name" : 'index.html', "cards": needed_page, "wcount" : workers_count, "pcount": projects_count, "cpcount": completed_projects_count}

    context['theme'] = 'light' if request.COOKIES.get('theme') is None else request.COOKIES.get('theme')
    response = render(request, 'index.html', context=context)
    response = set_cookie(response, theme=context['theme'])

    return response

def subProjects(request, pid):
    name = Projects.objects.get(pid=pid)
    data = Subprojects.objects.filter(pid=pid).filter(status='completed')
    vacs = Vacancies.objects.select_related('sid').filter(sid__pid=pid).values("vid", "post", "sid", "description")
    context= {"project" : name, "cards" : data, "vacancies": vacs}

    # Отправка почты
    if request.method == "POST":
        data = dict()
        form_names = ['name', 'second_name', 'group', 'email', 'subporject_name', 'vacancy', 'description']

        for name in form_names:
            data[name] = request.POST.get(name)
            send_form(data)

    context['theme'] = 'light' if request.COOKIES.get('theme') is None else request.COOKIES.get('theme')
    response = render(request, 'subProjects.html', context=context)
    response = set_cookie(response, theme=context['theme'])

    return response

def completedProjects(request):
    data = Subprojects.objects.select_related('pid').filter(status='completed').values('pid', 'pid__title', 'pid__description', 'pid__photo').distinct()
    data_paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    needed_page = data_paginator.get_page(page_number)

    context= {"template_name" : 'completedProjects.html', "cards": needed_page}

    context['theme'] = 'light' if request.COOKIES.get('theme') is None else request.COOKIES.get('theme')
    response = render(request, 'completedProjects.html', context=context)
    response = set_cookie(response, theme=context['theme'])

    return response

def cinema(request, pid):
    name = Projects.objects.get(pid=pid)
    data = WorkersInSubprojects.objects.select_related('sid', 'wid').filter(sid__pid=pid, sid__status='completed')
    context = {'project': name, 'cards': data}

    name.phone = format_phone(name)

    context['theme'] = 'light' if request.COOKIES.get('theme') is None else request.COOKIES.get('theme')
    response = render(request, 'cinema.html', context=context)
    response = set_cookie(response, theme=context['theme'])

    return response


def search(request):

    model = Projects.objects

    if request.GET.get('page') == 'Выполненные проекты':
        tmp = Subprojects.objects.select_related('pid').filter(status='completed').values('pid')
        pids = [dict['pid'] for dict in tmp]
        model = Projects.objects.filter(pid__in=pids)


    if request.method == 'GET':
        search_query = request.GET.get('search', '')

        if search_query:
            prj = model.filter(title__icontains=search_query)
        else:
            prj = model.all()

    response = serialize('json', list(prj), fields=('pid'))

    return JsonResponse(response, safe=False)