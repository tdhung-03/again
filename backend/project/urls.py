from django.urls import path 
from .views import *

urlpatterns = [
    path("", projects, name="projects"),
    path("project/<int:id>", project, name="project"),
    path("create-project/", create_project, name="create-project"),
]