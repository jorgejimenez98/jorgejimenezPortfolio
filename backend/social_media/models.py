from django.db import models
from main_settings.constants import LANGUAJES_CHOICES, CURRICULUM_CHOICES, ENGLISH, MODERN

class Curriculum(models.Model):
    name = models.CharField(max_length=255, choices=CURRICULUM_CHOICES, default=MODERN)
    language = models.CharField(max_length=2, choices=LANGUAJES_CHOICES, default=ENGLISH)
    link = models.URLField(default="")

    def __str__(self):
        return f'{self.name}-{self.language}-{self.link}'


class SocialMedia(models.Model):
    className = models.CharField(max_length=255)
    iconClassName = models.CharField(max_length=255)
    link = models.URLField(default="")

    def __str__(self):
        return f'{self.className} - {self.link}'