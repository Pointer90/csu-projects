from django.contrib import admin
from .models import Projects, Workers

# Register your models here.
@admin.register(Projects)
class Projects(admin.ModelAdmin):

    list_display = ['title', 'status', 'display_year', ]
    list_filter = ['status',]
    search_fields = ['creation_date', 'title__startswith', 'status']

    fields = (('title', 'status'), 'photo', 'description')

@admin.register(Workers)
class Workers(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name__startswith',]

