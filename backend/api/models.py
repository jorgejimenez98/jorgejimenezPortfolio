from django.db import models
from solo.models import SingletonModel

""" Site Configuration """


class SiteConfiguration(SingletonModel):
    developer_name = models.CharField(max_length=255, default="")
    main_presentation_text = models.TextField(default="")
    years_of_experience = models.PositiveIntegerField(default=0)
    is_open_to_work = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, default="")
    repository_project_url = models.URLField(default="")
    developer_email = models.EmailField(default="")

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"


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
    image_logo = models.ImageField(
        blank=True, null=True, upload_to=uploadTechPath)


""" Curriculum """


class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(default="")

    def __str__(self):
        return f'Curriculum {self.name}'
