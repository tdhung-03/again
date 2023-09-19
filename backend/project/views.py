from django.shortcuts import render, redirect
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
            return redirect("projects")
    context = {
        'form': form,
    }
    return render(request, "project/create_project.html", context)

def edit_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context = {
        'form': form,
    }
    return render(request, "project/edit_project.html", context)

def delete_project(request, id):
    project= Project.objects.get(id=id)
    if request.method == 'POST':
        project.delete()
        return redirect("projects")
    return render(request, "project/delete_project.html")