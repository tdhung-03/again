from django.shortcuts import render
from .models import *
# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, "project/projects.html", context)