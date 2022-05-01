from django.db import models


""" Social Media """


class SocialMedia(models.Model):
    className = models.CharField(max_length=255)
    iconClassName = models.CharField(max_length=255)
    link = models.URLField(default="")

    def __str__(self):
        return f'{self.className} - {self.link}'


""" Technologie """


class Main_Tech(models.Model):
    text = models.CharField(max_length=255)
    proccessPorcent = models.CharField(max_length=255)

    def __str__(self):
        return f'Main Tech {self.text} - {self.proccessPorcent}'


def uploadTechPath(x, filename):
    return '/'.join(['technology', filename])


class Technologie(models.Model):
    name = models.CharField(max_length=255)
    image_logo = models.ImageField(blank=True, null=True, upload_to=uploadTechPath)

    def __str__(self):
        return f'tech {self.name}'


""" Curriculum """


class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(default="")

    def __str__(self):
        return f'Curriculum {self.name}'


""" Projects """


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
