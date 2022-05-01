from django.db import models


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
