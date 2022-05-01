from django.db import models
from technologie.models import Technologie


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    repositoryUrl = models.URLField(default="", null=True)
    technologies = models.ManyToManyField(Technologie, related_name='projects')

    def __str__(self):
        return f'Project {self.name}'


def uploadProjectItemPath(x, filename):
    return '/'.join(['projectitems', filename])


class ProjectItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    image = models.ImageField(blank=True, null=True, upload_to=uploadProjectItemPath)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='projectItems')

    def __str__(self):
        return f'Project Item {self.title} - {self.project.name}'