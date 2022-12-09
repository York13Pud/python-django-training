from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def projects(request):
    message = "Hello World!"
    number = 50
    context = {"message": message,
               "number": number
              }
    
    return render(request, "projects/projects.html", context = context)


def project(request, key):
    return render(request, "projects/project.html")