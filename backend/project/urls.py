from django.urls import path 
from .views import *

urlpatterns = [
    path("", projects, name="projects"),
    path("project/<int:id>", project, name="project"),
]