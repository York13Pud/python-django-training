from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name = "profiles"),
    path('profile', views.profile, name = "user-profile"),
]
