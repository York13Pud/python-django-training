from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name = "projects"),
    path('project/<str:key>/', views.project, name = "project"),
    path('create-project/', views.create_project, name = "create-project"),
    path('update-project/<str:key>/', views.update_project, name = "update-project"),
    path('delete-project/<str:key>/', views.delete_project, name = "delete-project")
]
