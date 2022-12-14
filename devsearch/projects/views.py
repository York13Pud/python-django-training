from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import Project_Form


# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    #print(projects[1].tag.__dict__)
    return render(request, 
                  "projects/projects.html", 
                  context = context)


def project(request, key):
    project_obj = Project.objects.get(id = key)
    tags = project_obj.tag.all()
    return render(request, 
                  "projects/project.html", 
                  context = {"project": project_obj, "tags": tags})


@login_required(login_url = "login")
def create_project(request):
    profile = request.user.profile
    form = Project_Form
    context = {"form": form}
    
    # --- If the request is POST, check that the form is valid and then save it to the database:
    if request.method == "POST":
        form = Project_Form(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect("projects")   
        
    return render(request, "projects/project-form.html", context)


@login_required(login_url = "login")
def update_project(request, key):
    profile = request.user.profile
    project = profile.project_set.get(id = key) # --- Limits updating to the owner
    form = Project_Form(instance = project)
    context = {"form": form}
    
    # --- If the request is POST, check that the form is valid and then save it to the database:
    if request.method == "POST":
        # --- Passing instance = project will pre-populate the fields on the form with the current records data:
        form = Project_Form(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            return redirect("projects")
        
    return render(request, "projects/project-form.html", context)


@login_required(login_url = "login")
def delete_project(request, key):
    profile = request.user.profile
    project = profile.project_set.get(id = key) # --- Limits updating to the owner
    context = {"object": project}
    
    if request.method == "POST":
        # --- Passing instance = project will pre-populate the fields on the form with the current records data:
        project.delete()    
        return redirect("projects")
    
    return render(request, "projects/delete-template.html", context)