from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Profile
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
            return redirect("projects")
    context = {
        'form': form,
    }
    return render(request, "user/signup.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("projects")
    return render(request, "user/login.html")


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("projects")
    return render(request, "user/logout_user.html")


@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, "user/account.html", context)
