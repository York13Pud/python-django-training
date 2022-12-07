from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name = "projects"),
    path('project/<str:key>/', views.project, name = "project")
]
