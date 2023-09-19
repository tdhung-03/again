from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)   

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    demo_link = models.CharField(max_length=200,null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title