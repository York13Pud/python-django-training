from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name = "projects"),
    path('project/<str:key>/', views.project, name = "project")
]
