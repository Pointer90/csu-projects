from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Projects)
class Projects(admin.ModelAdmin):
    list_filter = ('project_created',)

    list_display = ['project_name', 'project_description', 'project_created']

    fieldsets = (
        (None, {
            'fields': (('project_name', 'project_preview'),)
        }),
        (None, {
            'fields': ('project_description',)
        })
    )


@admin.register(SubProjects)
class SubProjects(admin.ModelAdmin):
    list_filter = ('subproject_created',)

    list_display = ['project_id',
                    'subproject_name',
                    'subproject_description',
                    'subproject_created'
                    ]

    fieldsets = (
        (None, {
            'fields': (('project_id', 'subproject_name'),)
        }),
        (None, {
            'fields': ('subproject_description',)
        })
    )


@admin.register(SubProjectNeeds)
class SubProjectNeeds(admin.ModelAdmin):
    list_filter = ('need_profiles',)
    list_display = ['subproject_id', 'need_profiles', 'need_description']

    fields = ('subproject_id', 'need_profiles', 'need_description')


@admin.register(CompletedProjects)
class CompletedProjects(admin.ModelAdmin):
    list_filter = ('comp_project_created',)

    list_display = ['comp_project_name',
                    'comp_project_description',
                    'comp_project_created'
                    ]

    fieldsets = (
        (None, {
            'fields': ('comp_project_name', 'comp_project_preview',)
        }),
        (None, {
            'fields': ('comp_project_description',)
        })
    )


@admin.register(Workers)
class Workers(admin.ModelAdmin):
    list_display = ['worker_full_name']


@admin.register(WorkersInProject)
class WorkersInProject(admin.ModelAdmin):
    list_filter = ('worker_post',)
    list_display = ['worker_id',
                    'worker_post',
                    'comp_project_id',
                    'worker_description'
                    ]
    fieldsets = (
        ('Данные работника', {
            'fields': (('worker_id', 'worker_post'),)
        }),
        ('Данные проекта', {
            'fields': ('comp_project_id', 'worker_description')
        }),
    )
