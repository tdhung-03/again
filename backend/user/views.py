from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def profile(request, id):
    profile = Profile.objects.get(id=id)
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'projects': projects,
    }   
    return render(request, "user/profile.html", context)

def create_user(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profile")
    context = {
        'form': form,
    }
    return render(request, "user/create_user.html", context)

def login_user(request):
    username = ""
    password = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("projects")
    context = {

    }
    return render(request, "user/login_user.html", context)

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("projects")
    context = {

    }
    return render(request, "user/logout_user.html", context)