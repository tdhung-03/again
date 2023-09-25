from django.urls import path
from .views import projects, project, create_project, edit_project, delete_project

urlpatterns = [
    path("", projects, name="projects"),
    path("project/<int:id>", project, name="project"),
    path("create-project/", create_project, name="create-project"),
    path("edit-project/<int:id>", edit_project, name="edit-project"),
    path("delete-project/<int:id>", delete_project, name="delete-project"),
]
