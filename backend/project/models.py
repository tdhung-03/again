from django.db import models
from user.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    featured_image = models.ImageField(null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
