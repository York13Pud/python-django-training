from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def projects(request):
    message = "Hello World!"
    return render(request, "projects/projects.html", {"message": message})


def project(request, key):
    return render(request, "projects/project.html")