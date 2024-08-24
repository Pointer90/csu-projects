from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Projects, Workers, Subprojects, Vacancies, WorkersInSubprojects
from .smtp_server import send_form
from .forms import ShareProjectForm, SubprojectForm

# Create your views here.


def main(request: HttpRequest):
    pids = request.session.pop('pids', None)
    check_form = request.session.pop('is_form_valid', None)

    if pids is None:
        data = Projects.objects.exclude(status='completed').exclude(status='frozen')
    else:
        data = Projects.get_projects_by_pid(pids)

    data_paginator = Paginator(data, 10)
    page_number = request.GET.get("page")

    context = {
        'page': f'{request.get_full_path()}main',
        'cards': data_paginator.get_page(page_number),
        'wcount': Workers.objects.count(),
        'pcount': Projects.objects.count(),
        'cpcount': Projects.objects.filter(status='completed').count(),
        'isFound': True if data.count() > 0 else False,
        'form': {'body': ShareProjectForm(), 'title': 'Предложить проект', 'btn_text': 'Отправить'},
        'notify': notify(check_form),
    }

    request.session.clear()

    return render(request, 'pages/index.html', context=context)


def subProjects(request: HttpRequest, pid):
    check_form = request.session.pop('is_form_valid', None)

    context = {
        'page': f'{request.get_full_path()}',
        'project': Projects.get_projects_by_pid([pid])[0],
        'cards': Subprojects.objects.filter(pid=pid).exclude(status='completed'),
        'vacancies': Vacancies.objects
                .select_related('sid')
                .filter(sid__pid=pid)
                .values('vid', 'post', 'sid', 'description'),
        'form': {'body': SubprojectForm(pid=pid),
                 'title': 'Записаться на проект',
                 'btn_text': 'Записаться'},
        'notify': notify(check_form),
    }

    request.session.clear()

    return render(request, 'pages/subProjects.html', context=context)


def completedProjects(request: HttpRequest):
    pids = request.session.pop('pids', None)

    if pids is None:
        data = Projects.get_partially_completed_projects()
    else:
        data = Projects.get_projects_by_pid(pids)

    data_paginator = Paginator(data, 10)
    page_number = request.GET.get('page')

    context = {
        'page': request.get_full_path(),
        'isFound': True if data.count() > 0 else False,
        'cards': data_paginator.get_page(page_number),
    }

    request.session.clear()

    return render(request, 'pages/completedProjects.html', context=context)


def cinema(request: HttpRequest, pid):
    context = {
        'project': Projects.get_projects_by_pid([pid])[0],
        'cards': WorkersInSubprojects.objects.select_related('sid', 'wid').filter(sid__pid=pid, sid__status='completed')
    }

    return render(request, 'pages/cinema.html', context=context)

# ---- API ednpoits ----


def api_search(request: HttpRequest):
    redirect_func = redirect(main)

    if request.method == 'GET':
        search_query = request.GET.get('search', '')
        path_page = request.GET.get('page-query').split('/')

        if search_query:
            if 'completedProjects' in path_page:
                pids = Projects.objects.filter(
                    pid__in=Subprojects.objects.select_related('pid').filter(status='completed').values('pid'),
                    title__icontains=search_query
                ).values('pid')
                redirect_func = redirect(completedProjects)

            if 'main' in path_page:
                pids = Projects.objects.exclude(status='completed').exclude(status='frozen').filter(title__icontains=search_query).values('pid')

            request.session['pids'] = [dict['pid'] for dict in pids]
        else:
            request.session['pids'] = None

    return redirect_func


def api_post_form(request: HttpRequest):
    redirect_func = redirect(main)

    try:
        if request.method == 'POST':
            path_query = request.POST.get('page-query').split('/')

            if 'main' in path_query:
                form = ShareProjectForm(request.POST)

            elif 'subProjects' in path_query:
                pid = int(path_query[-1])
                form = SubprojectForm(pid=pid, data=request.POST)
                redirect_func = redirect(subProjects, pid)
            else:
                raise ValueError

            if form.is_valid():
                send_form(form.cleaned_data)
                request.session['is_form_valid'] = 200
            else:
                request.session['is_form_valid'] = 300

            return redirect_func

        else:
            raise ValueError

    except ValueError:
        request.session['is_form_valid'] = 500
        return redirect_func


# ---- Services ----

def notify(status, msg: str = None) -> dict:
    notify = {'is_active': False}

    if status is not None:
        notify.update({'is_active': True})

        if status == 200:
            notify.update({'type': 'Успех', 'body': 'данные отправлены.', 'status': 'success'})

        elif status == 300:
            notify.update({'type': 'Внимание', 'body': 'некорректные данные.', 'status': 'warning'})

        elif status == 500:
            notify.update({'type': 'Ошибка', 'body': 'данные не отправлены.', 'status': 'danger'})

        if msg is not None:
            notify.update({'body': msg})

    return notify
