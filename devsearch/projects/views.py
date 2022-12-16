from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import Project_Form

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    
    return render(request, 
                  "projects/projects.html", 
                  context = context)


def project(request, key):
    project_obj = Project.objects.get(id = key)
    tags = project_obj.tag.all()
    return render(request, 
                  "projects/project.html", 
                  context = {"project_obj": project_obj, "tags": tags})
    

def create_project(request):
    form = Project_Form
    context = {"form": form}
    return render(request, "projects/project-form.html", context)