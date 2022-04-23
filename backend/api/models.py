from django.db import models
from datetime import date


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


""" Experience """


class KeyExperience(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'Key Experience {self.text}'


class TechnologieItem(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'Technologie Item {self.text}'


def uploadExperiencePath(x, filename):
    return '/'.join(['experience', filename])


class Experience(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    is_currently_working = models.BooleanField(default=False)
    company_logo = models.ImageField(blank=True, null=True, upload_to=uploadExperiencePath)
    job_rol = models.CharField(max_length=255)
    conmpany_name = models.CharField(max_length=255)
    description = models.TextField(default="")
    key_experiences = models.ManyToManyField(KeyExperience, related_name='experiences_key')
    techs = models.ManyToManyField(TechnologieItem, related_name='experiences_items')

    def __str__(self):
        return f'Experience {self.job_rol} - {self.conmpany_name}'

    def get_time_working(self):
        if self.is_currently_working:
            return date.today() - self.date_start
        return self.date_end - self.date_start
