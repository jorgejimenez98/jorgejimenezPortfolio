from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(default="")

    def __str__(self):
        return f'Curriculum {self.name}'


class SocialMedia(models.Model):
    className = models.CharField(max_length=255)
    iconClassName = models.CharField(max_length=255)
    link = models.URLField(default="")

    def __str__(self):
        return f'{self.className} - {self.link}'