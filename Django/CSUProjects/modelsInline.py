from django.contrib import admin
from .models import *
from django import forms

class SubProjectsInline(admin.TabularInline):
    model = SubProjects
    extra = 0

    fields = ('subprj_name', 'status', 'subprj_preview', 'subprj_description',)
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 10, 'cols': 40})},
    }

class SubProjectNeedsInline(admin.TabularInline):
    model = SubProjectNeeds
    extra = 0

class WorkerInline(admin.TabularInline):
    model = Workers
    extra = 0