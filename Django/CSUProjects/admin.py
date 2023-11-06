from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Projects)
admin.site.register(SubProjects)
admin.site.register(SubProjectNeeds)
admin.site.register(CompletedProjects)
admin.site.register(Workers)
admin.site.register(WorkersInProject)