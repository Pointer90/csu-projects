from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Projects)
admin.site.register(Subprojects)
admin.site.register(Subproject_needs)
admin.site.register(Completed_projects)
admin.site.register(Workers)