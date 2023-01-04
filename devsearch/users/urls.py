from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name = "profiles"),
    path('user-profile/<str:pk>/', views.user_profile, name = "user-profile"),
    path('login/', views.login_page, name = "login"),
]
