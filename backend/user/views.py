from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile
# Create your views here.


def profile(request, id):
    profile = Profile.objects.get(id=id)
    projects = profile.projects.all()
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
    if request.user.is_authenticated:
        return redirect('account')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("projects")
    return render(request, "user/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, "user/account.html", context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        'form': form,
    }
    return render(request, "user/edit_account.html", context)
