from django.contrib import admin
from .models import *
from .modelsInline import SubProjectNeedsInline, SubProjectsInline
# Register your models here.



@admin.register(Projects)
class Projects(admin.ModelAdmin):

    list_display = ['prj_name', 'status', 'display_year', ]
    list_filter = ['status',]
    search_fields = ['prj_created', 'prj_name__startswith', 'status']

    fields = (('prj_name', 'status'), 'prj_preview', 'prj_description')

    inlines = [SubProjectsInline]

@admin.register(SubProjects)
class SubProjects(admin.ModelAdmin):
    list_filter = ('subprj_created',)
    list_display = ['prj_id',
                    'subprj_name',
                    'subprj_description',
                    'subprj_created'
                    ]

    fields = (('subprj_name', 'status'), 'subprj_preview', 'subprj_description')

    inlines = [SubProjectNeedsInline,]


@admin.register(SubProjectNeeds)
class SubProjectNeeds(admin.ModelAdmin):
    list_filter = ('need_profiles',)
    list_display = ['subprj_id', 'need_profiles', 'need_description']

    fields = ('subprj_id', 'need_profiles', 'need_description')

@admin.register(Workers)
class Workers(admin.ModelAdmin):
    list_display = ['worker_full_name']
    search_fields = ['worker_full_name__startswith',]


@admin.register(WorkersInProject)
class WorkersInProject(admin.ModelAdmin):
    list_filter = ('worker_post', 'prj_id')
    list_display = ['worker_id',
                    'worker_post',
                    'prj_id',
                    ]
    fieldsets = (
        ('Данные работника', {
            'fields': (('worker_id', 'worker_post'),)
        }),
        ('Данные проекта', {
            'fields': ('prj_id', 'worker_description')
        }),
    )
