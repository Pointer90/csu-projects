from django.contrib import admin
from django import forms

from django.db import models
from .models import Projects, Workers, Subprojects, Vacancies, WorkersInSubprojects

# TabularInlines


class SubprojectsInline(admin.TabularInline):
    model = Subprojects
    extra = 0

    fields = ('title', 'status', 'description')
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 5, 'cols': 70})},
    }


class VacanciesInline(admin.TabularInline):
    model = Vacancies
    extra = 0

    fields = ('post', 'description')
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 5, 'cols': 70})},
    }


class WorkersInSubprojectsInlines(admin.TabularInline):
    model = WorkersInSubprojects
    extra = 0

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 5, 'cols': 70})},
    }

# Register models


@admin.register(Projects)
class Projects(admin.ModelAdmin):

    list_display = ['title', 'status', 'display_year',]
    list_filter = ['status',]
    search_fields = ['creation_date', 'title__startswith', 'status']

    fields = (('title', 'status'), 'phone', 'link', 'photo', 'description', 'rating')
    inlines = [SubprojectsInline]


@admin.register(Workers)
class Workers(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name__startswith',]


@admin.register(Subprojects)
class SubProjects(admin.ModelAdmin):
    list_filter = ('creation_date',)
    list_display = ['pid', 'title', 'description', 'creation_date']

    fields = (('title', 'status'), 'photo', 'description')
    inlines = [VacanciesInline, WorkersInSubprojectsInlines]


# @admin.register(Vacancies)
class SubProjectNeeds(admin.ModelAdmin):
    list_filter = ('post',)
    list_display = ['sid', 'post', 'description']

    fields = ('sid', 'post', 'description')


# @admin.register(WorkersInSubprojects)
class WorkersInSubprojects(admin.ModelAdmin):

    list_display = ['sid', 'wid', 'post', 'description']
