from django.shortcuts import render, redirect
from .forms import *
# Create your views here.


def profile(request):
    context = {

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