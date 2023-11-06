from django.urls import path
from . import views

from Django import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="main"),
    path('subProjects/<int:project_id>', views.subProjects, name='subProjects'),
    path('completedProjects', views.completedProjects, name='completedProjects'),
    path('cinema/<int:comp_project_id>', views.cinema, name='cinema'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)