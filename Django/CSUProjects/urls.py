from django.urls import path
from . import views

from Django import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="main"),
    path('subProjects/<int:pid>', views.subProjects, name='subProjects'),
    path('completedProjects', views.completedProjects, name='completedProjects'),
    path('cinema/<int:pid>', views.cinema, name='cinema'),
    path('search', views.search, name='search'),
    path('sendLetter', views.sendLetter, name='sendLetter'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)