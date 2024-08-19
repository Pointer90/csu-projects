from django.urls import path
from . import views

from Config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name="main"),
    path('subProjects/<int:pid>', views.subProjects, name='subProjects'),
    path('completedProjects', views.completedProjects, name='completedProjects'),
    path('cinema/<int:pid>', views.cinema, name='cinema'),
    path('api/api_search', views.api_search, name='api_search'),
    path('api/postForm', views.api_post_form, name='api_post_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
