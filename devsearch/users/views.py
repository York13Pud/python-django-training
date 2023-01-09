from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.


def login_user(request):
    page = "login"
    
    # --- This will redirect a logged in user to profiles if they try
    # --- to access the login page directly.
    if request.user.is_authenticated:
        return redirect(to = "profiles")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request = request,
                           message= "Username does not exist")
        
        user = authenticate(request = request,
                            username = username,
                            password = password)
        
        if user is not None:
            login(request, user = user)
            return redirect("profiles")
        else:
            messages.error(request = request,
                           message= "Username or password is incorrect")
    
    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request = request)
    messages.info(request = request, 
                  message= "You were successfully logged out")
    return redirect(to = "login")


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        # --- The below will check if the form is valid. If so, it will
        # --- save tbe form data temporarily, set the username to lowercase,
        # --- save the user in the database, create a profile (signal),
        # --- return a success message and log the user in.
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request = request, 
                             message = "User account created!")

            login(request = request, user = user)
            return redirect(to = "profiles")
        
        # --- If the form is not valid, the user will get an error message.
        else:
            messages.error(request = request, 
                           message = "An error ocurred during registration. Please try again.")
            
    context = {"page": page,
               "form": form}
    
    return render(request = request, 
                  template_name = "users/login_register.html", 
                  context = context)


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


def user_account(request, pk):
    profile = Profile.objects.get(id = pk)
    context = {}
    return render(request = request, 
                  template_name = "users/account.html", 
                  context = context)

    
def edit_account(request):
    context = {}
    return render(request, "users/user-profile.html", context = context)


def create_skill(request):
    context = {}
    return render(request, "users/user-profile.html", context = context)