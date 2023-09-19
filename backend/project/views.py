from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, "project/projects.html", context)

def project(request, id):
    project = Project.objects.get(id=id)
    tags = project.tags.all()
    context = {
        'project': project,
        'tags': tags
    }
    return render(request, "project/project.html", context)

def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, "project/create_project.html", context)