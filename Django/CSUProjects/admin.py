from django.contrib import admin
from .models import *
from django import forms

# Register your models here.

class SubProjectsInline(admin.TabularInline):
    model = SubProjects
    extra = 0

    fields = ('subprj_name', 'status', 'subprj_preview', 'subprj_description')
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 10, 'cols': 40})},
    }


@admin.register(Projects)
class Projects(admin.ModelAdmin):

    list_display = ['prj_name', 'prj_description', 'prj_created', 'status']
    list_filter = ('prj_created', )

    fields = (('prj_name', 'status'), 'prj_preview', 'prj_description')

    inlines = [SubProjectsInline]


class SubProjects(admin.ModelAdmin):
    list_filter = ('subprj_created',)

    list_display = ['prj_id',
                    'subprj_name',
                    'subprj_description',
                    'subprj_created'
                    ]

    fields = (('subprj_name', 'status'), 'subprj_preview', 'subprj_description')


@admin.register(SubProjectNeeds)
class SubProjectNeeds(admin.ModelAdmin):
    list_filter = ('need_profiles',)
    list_display = ['subprj_id', 'need_profiles', 'need_description']

    fields = ('subprj_id', 'need_profiles', 'need_description')



@admin.register(Workers)
class Workers(admin.ModelAdmin):
    list_display = ['worker_full_name']


@admin.register(WorkersInProject)
class WorkersInProject(admin.ModelAdmin):
    list_filter = ('worker_post',)
    list_display = ['worker_id',
                    'worker_post',
                    'prj_id',
                    'worker_description'
                    ]
    fieldsets = (
        ('Данные работника', {
            'fields': (('worker_id', 'worker_post'),)
        }),
        ('Данные проекта', {
            'fields': ('prj_id', 'worker_description')
        }),
    )
