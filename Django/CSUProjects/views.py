from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Projects, Workers, Subprojects, Vacancies, WorkersInSubprojects
from .smtp_server import send_form
from .forms import ShareProjectForm, SubprojectForm

# Create your views here.

def main(request):
    pids = request.session.pop('pids', None)

    if pids is not None:
        data = Projects.get_projects_by_pid(pids)
    else:
        data = Projects.objects.exclude(status='completed').exclude(status='frozen')

    data_paginator = Paginator(data, 2)
    page_number = request.GET.get("page")

    context = {
        'page': 'main',
        'cards': data_paginator.get_page(page_number),
        'wcount': Workers.objects.count(),
        'pcount': Projects.objects.count(),
        'cpcount': Projects.objects.filter(status='completed').count(),
        'form': {'body':ShareProjectForm(), 'title': 'Предложить проект', 'btn_text': 'Отправить'}
    }

    return render(request, 'pages/index.html', context=context)


def subProjects(request, pid):
    context= {
        'page': 'subProjects',
        'project' : Projects.get_projects_by_pid([pid]),
        'cards' : Subprojects.objects.filter(pid=pid).exclude(status='completed'),
        'vacancies': Vacancies.objects.select_related('sid').filter(sid__pid=pid).values('vid', 'post', 'sid', 'description'),
        'form': {'body': SubprojectForm(pid=pid), 'title': 'Записаться на проект', 'btn_text': 'Записаться'}
    }

    return render(request, 'pages/subProjects.html', context=context)


def completedProjects(request):
    pids = request.session.pop('pids', None)

    if pids is not None:
        data = Projects.get_projects_by_pid(pids)
    else:
        data = Projects.get_partially_completed_projects()

    data_paginator = Paginator(data, 10)
    page_number = request.GET.get('page')

    context= {
        'page': 'completedProjects',
        'cards': data_paginator.get_page(page_number),
    }

    return render(request, 'pages/completedProjects.html', context=context)


def cinema(request, pid):
    context = {
        'project': Projects.get_projects_by_pid([pid])[0],
        'cards': WorkersInSubprojects.objects.select_related('sid', 'wid').filter(sid__pid=pid, sid__status='completed')
    }

    return render(request, 'pages/cinema.html', context=context)

# ---- API ednpoits ----
def search(request):
    url = reverse('main')

    if request.method == 'GET':
        pids = []

        search_query = request.GET.get('search', '').lower()
        page = request.GET.get('page-query')

        if search_query:
            if page == 'completedProjects':
                tmp = Subprojects.objects.select_related('pid').filter(status='completed').values('pid')
                
                pids = Projects.objects.filter(
                    pid__in=tmp,
                    title__icontains=search_query
                ).values('pid')

            if page == 'main':
                pids = Projects.objects.filter(title__icontains=search_query).values('pid')

            request.session['pids'] = [dict['pid'] for dict in pids]
        else:
            request.session['pids'] = None

        url = reverse(page)

    return redirect(url)


def sendLetter(request):
    

    if request.method == "POST":
        page = request.POST.get('page-query')

        if page == 'main':
            form_names = ['title_project', 'title_organization', 'email', 'vacancy', 'description']
        elif page == 'subProjects':
            form_names = ['name', 'second_name', 'group', 'email', 'subporject_name', 'vacancy', 'description']
        else:
            return HttpResponse('Invalid argument', status=422)


        data = dict()
        
        for name in form_names:
            data[name] = request.POST.get(name)

        # send_form(data)

        return HttpResponse('Form submitted successfully', status=200)
    else:
        return HttpResponse(status=403)