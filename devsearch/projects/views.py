from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
projects_list = [
                 {'id': '1', 
                  'title': 'Ecommerce Website', 
                  'description': 'Fully functional ecommerce website'
                 }, 
                 {'id': '2', 
                  'title': 'Portfolio Website', 
                  'description': 'A personal website to write articles and display work'
                 },
                 {'id': '3', 
                  'title': 'Social Network', 
                  'description': 'An open source project built by the community'
                 }
                ]


def projects(request):
    message = "Hello World!"
    number = 48
    context = {"message": message,
               "number": number,
               "projects": projects_list
              }
    
    return render(request, "projects/projects.html", context = context)


def project(request, key):
    project_id = None
    for id in projects_list:
        if id["id"] == key:
            project_id = id
    return render(request, "projects/project.html", context = {"project": project_id})