from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

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


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect("projects")
    context = {
        'form': form,
    }
    return render(request, "project/create_project.html", context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        project.delete()
        return redirect("projects")
    return render(request, "project/delete_project.html")
