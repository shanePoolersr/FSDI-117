from django.urls import path
from projects import views

urlpatterns = [
    path('', views.project_new, name='projects_list'),
]