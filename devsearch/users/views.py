from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        try:
            user = User.objects.get(username = username)
        except:
            print("Username does not exist")
        
        user = authenticate(request = request,
                            username = username,
                            password = password)
        
        if user is not None:
            login(request, user = user)
            return redirect("profiles")
        else:
            print("Username or password is incorrect")
    
    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request = request)
    return redirect(to = "login")

def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context = context)


def user_profile(request, pk):
    profile = Profile.objects.get(id = pk)
    skills = profile.skill_set.exclude(description__exact = "") # Any description that is blank is ignored.
    other_skills = profile.skill_set.filter(description="")
    
    context = {"profile": profile,
               "top_skills": skills,
               "other_skills": other_skills}
    
    return render(request, "users/user-profile.html", context = context)