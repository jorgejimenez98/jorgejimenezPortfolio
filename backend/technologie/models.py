from django.db import models
from main_settings.models import TranslationText


class Main_Tech(models.Model):
    texts = models.ManyToManyField(TranslationText, related_name='main_techs')
    proccessPorcent = models.CharField(max_length=255)

    def __str__(self):
        return f'Main Tech {self.pk}'


def uploadTechPath(x, filename):
    return '/'.join(['technology', filename])


class Technologie(models.Model):
    name = models.CharField(max_length=255)
    image_logo = models.ImageField(
        blank=True, null=True, upload_to=uploadTechPath)
    icon_class = models.CharField(max_length=255, default="")

    def __str__(self):
        return f'tech {self.name}'

    @property
    def has_logo(self):
        return not (len(str(self.icon_class).strip()) > 0 and self.image_logo is not None)


class TechnologieItem(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
