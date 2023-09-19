from django.urls import path 
from .views import *

urlpatterns = [
    path("", projects, name="projects"),
    path("project/<int:id>", project, name="project"),
    path("create-project/", create_project, name="create-project"),
    path("edit-project/<int:id>", edit_project, name="edit-project"),
    path("delete-project/<int:id>", delete_project, name="delete-project"),
]